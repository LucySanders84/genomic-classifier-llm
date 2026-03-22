import re
import random

from typing_extensions import Pattern

from classes.PipelineParameters import PipelineParameters
from data_pipeline.pipeline_lib.fragments import fragments
from data_pipeline.pipeline_lib.sequence_source import chromosome_dict
from data_pipeline.pipeline_lib.sequences import build_sequences


def build(data_source_parameters: dict[str, dict[str, str | Pattern ]], input_parameters: dict[str, int]) -> dict[str, list[str]]:
    """Builds inputs for datasets based on data source and input parameters.

    Performs the following operations:
         - Builds a sequence source dictionary based on data source parameters.
         - Builds a pipeline parameters object from data source and input parameters.
         - Gets sequences for each group represented in the dataset.
         - Builds fragment list from sequences.
    Args:
        data_source_parameters: parameter settings for obtaining data from source
        input_parameters: parameter settings for the types of inputs to build for this dataset

    Returns: list of fragments created from sequences sourced from data source and conforming to input parameters.
    """

    # build sequence source dict
    chromosomes = chromosome_dict.build(
        data_source_parameters['ss']['filename'],
        data_source_parameters['ss']['id_pattern'])

    # build pipeline parameters for input groups
    pipeline_params = []
    for i in range(len(data_source_parameters['labels'].keys())):
        j = str(i)
        pipeline_params.append(
            PipelineParameters(
                label=data_source_parameters["labels"][j],
                sequence_source=chromosomes,
                feature_source_filename=data_source_parameters['fsf'][j],
                target_type=data_source_parameters['target'][j],
                fragment_length=input_parameters['length'],
                stride=input_parameters['stride']
            ))

    # get sequences for each group
    seq_lists = {}
    for params in pipeline_params:
        seq_lists[params.label] = build_sequences.run(
            params.feature_source_filename,
            params.target_type,
            chromosomes)

    # build fragments
    fragment_lists = {}
    for key in seq_lists.keys():
        fragment_lists[key] = fragments.build(seq_lists[key], input_parameters['length'], input_parameters['stride'])

    return fragment_lists


def validate(inputs: dict[str, list[str]], max_n_percentage, expected_length) -> dict[str,list[str]]:
    """Validates fragment length, alphabet, and a label presence to
    return a list of TSV-formatted strings.
    """
    validated_data = {}
    valid_dna_pattern = re.compile(r'^[ACGTN]+$', re.IGNORECASE)
    #check for missing labels or empty sequences
    for label in inputs:
        validated_data[label] = []
        for fragment in inputs[label]:
            if not label or not fragment:
                continue
            #length from constants.py
            if len(fragment) != expected_length:
                continue
            #ensure no weird characters from GFF/Fasta
            if not valid_dna_pattern.match(fragment):
                continue
            #drop sequences with mostly 'N' gaps
            n_count = fragment.upper().count('N')
            if (n_count / expected_length) > max_n_percentage:
                continue
            #if all pass, format as TSV string for the splitting step
            validated_data[label].append(fragment)

    return validated_data


def balance(validated_data: dict[str, list[str]]):

    # Random seed added to ensure that data split remains consistent across randomized trials
    random.seed()

    if not validated_data:
        print("No data to process.")
        return

    # This section finds the fragment grouping with the lowest sample size
    counts = {label: len(samples) for label, samples in validated_data.items()}
    min_count = min(counts.values())
    print(f"Class distribution: {counts}")
    print(f"Balancing dataset to {min_count} samples per class.")

    # From here, we use the minimum count to randomly shuffle and create lists for training
    balanced_list = []
    for label in validated_data:
        random_fragments = random.sample(validated_data[label], min_count)
        balanced_list = [*balanced_list, *[(fragment, label) for fragment in random_fragments]]
    # Line shuffles the lists to ensure a unique product each time
    random.shuffle(balanced_list)

    # Calculating split indices for training sets at 80%, 10%, then 10%, respectively
    # Note - this is where I first thought of the N problem, will discuss at next meeting - Jessi
    total = len(balanced_list)
    train_end = int(total * 0.8)
    val_end = train_end + int(total * 0.1)

    return {
        "train": balanced_list[:train_end],
        "val": balanced_list[train_end:val_end],
        "test": balanced_list[val_end:]
    }



