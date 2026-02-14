from typing_extensions import Pattern

from classes.PipelineParameters import PipelineParameters

from data_pipeline.pipeline_lib.sequence_source import chromosome_dict
from data_pipeline.pipeline_lib.fragments import fragments
from data_pipeline.pipeline_lib.sequences import build_sequences

"""
definitions:
input - a line item in a dataset used to train LLM
sequence - a string of base pairs
fragment - a sequence split from a larger sequence
"""


def validate_code_placeholder(inputs: list[tuple]):
    #placeholder func to be replaced
    return [f'{fragment}\t{label}\n' for fragment, label in inputs]


def run(data_source_parameters: dict[str, dict[str, str | Pattern ]], input_parameters: dict[str, int]):

    # build fragments with sequences and labels -> OUTPUT list[tuple(sequence: str, label:str)

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
    inputs: list[tuple] = []
    for label in fragment_lists.keys():
        for fragment in fragment_lists[label]:
            inputs.append(tuple([fragment, label]))
    pass

    # INPUT list[tuple(sequence: str, label:str)
    #   -> validate fragment output
    #       -> OUTPUT list[str (values separated by tabs)]

    # INPUT list[str (values separated by tabs)]
    #   -> balance 1 and 0 inputs across train, test, val sets
    #       -> WRITE TO FILE

    pass

from data_pipeline.constants import expected_length, max_n_percentage
import re

def validate_fragments(inputs: list[tuple[str, str]]) -> list[str]:
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
    
