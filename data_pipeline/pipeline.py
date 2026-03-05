
from typing_extensions import Pattern

from data_pipeline import exons_introns_pipeline
from data_pipeline.constants import DATA_PATH
from data_pipeline.pipeline_lib import datasets
from data_pipeline.pipeline_lib.inputs import inputs as inputs_lib

"""
definitions:
input - a line item in a dataset used to train LLM
sequence - a string of base pairs
fragment - a sequence split from a larger sequence
"""




def run(data_source_parameters: dict[str, dict[str, str | Pattern ]], input_parameters: dict[str, int]):

    # INPUT parameters for data source and inputs
    #   -> build fragments with sequences and labels
    #       -> OUTPUT list[tuple[sequence: str, label:str]]

    inputs = inputs_lib.build(data_source_parameters, input_parameters)
    for label in inputs:
        print(f'Group {label}: {len(inputs[label])} inputs passed validation steps')
    for key in data_source_parameters["fsf"].keys():
        print("\t", data_source_parameters["fsf"][key])

    # INPUT list[tuple(sequence: str, label:str)
    #   -> validate fragment output
    #       -> OUTPUT list[str (values separated by tabs)]
    validated_data = inputs_lib.validate(inputs, input_parameters["max_n_percentage"], input_parameters["length"])

    # INPUT list[str (values separated by tabs)]
    # balance 1 and 0 inputs across train, test, val sets
    data_splits = inputs_lib.balance(validated_data)
    # WRITE TO FILE
    datasets.write_from_data_splits(data_splits, DATA_PATH, 'csv', ',', '\n')

    pass


# Balance and Split Genomics Data
import random
import os


# This group separates out how many coding and non-coding fragments are actually present


if __name__ == '__main__':
    #runs exons and introns pipeline as default
    exons_introns_pipeline.run()


    
