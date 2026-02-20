import re
import random
import os

from typing_extensions import Pattern

from classes.PipelineParameters import PipelineParameters
from data_pipeline.pipeline_lib.fragments import fragments
from data_pipeline.pipeline_lib.sequence_source import chromosome_dict
from data_pipeline.pipeline_lib.sequences import build_sequences


def build(data_source_parameters: dict[str, dict[str, str | Pattern ]], input_parameters: dict[str, int]) -> list[tuple[str, str]]:
    # build fragments with sequences and labels -> OUTPUT list[tuple(sequence: str, label:str)

    #build sequence source dict
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

    # build sequence/label tuples list
    return [(fragment, label) for label in fragment_lists.keys() for fragment in fragment_lists[label]]


def validate(inputs: list[tuple[str, str]], max_n_percentage, expected_length) -> list[str]:
    """Validates fragment length, alphabet, and a label presence to
    return a list of TSV-formatted strings.
    """
    validated_data = []
    valid_dna_pattern = re.compile(r'^[ACGTN]+$', re.IGNORECASE)
    #check for missing labels or empty sequences
    for fragment, label in inputs:
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
        validated_data.append(f"{fragment}\t{label}\n")

    return validated_data


# Balance and Split Genomics Data
def balance_and_split_data(validated_data: list[str], output_dir):
    # Note - let me know if you want me to rename the output something else - Jessi

    # Random seed added to ensure that data split remains consistent across randomized trials
    random.seed()

    # This group separates out how many coding and non-coding fragments are actually present
    label_groups = {}
    for line in validated_data:
        label = line.strip().split('\t')[1]
        if label not in label_groups:
            label_groups[label] = []
        label_groups[label].append(line)

    if not label_groups:
        print("No data to process.")
        return

    # This section finds the fragment grouping with the lowest sample size
    counts = {label: len(samples) for label, samples in label_groups.items()}
    min_count = min(counts.values())
    print(f"Class distribution: {counts}")
    print(f"Balancing dataset to {min_count} samples per class.")

    # From here, we use the minimum count to randomly shuffle and create lists for training
    balanced_list = []
    for label in label_groups:
        balanced_list.extend(random.sample(label_groups[label], min_count))
    # Line shuffles the lists to ensure a unique product each time
    random.shuffle(balanced_list)

    # Calculating split indices for training sets at 80%, 10%, then 10%, respectively
    # Note - this is where I first thought of the N problem, will discuss at next meeting - Jessi
    total = len(balanced_list)
    train_end = int(total * 0.8)
    val_end = train_end + int(total * 0.1)

    data_splits = {
        "train.tsv": balanced_list[:train_end],
        "val.tsv": balanced_list[train_end:val_end],
        "test.tsv": balanced_list[val_end:]
    }

    # This writes to file system
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename, data in data_splits.items():
        path = os.path.join(output_dir, filename)
        with open(path, 'w') as f:
            f.writelines(data)
        print(f"Successfully created {len(data)} with training data sequences to {path}")