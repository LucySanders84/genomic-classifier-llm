"""
Pipeline module for obtaining and preprocessing data, building balanced datasets and writing dataset files to disk.

Pipeline definitions:
    input: a line item in a dataset used to train LLM.\n
    sequence: a string of base pairs.\n
    fragment: a sequence split from a larger sequence.
"""

from typing_extensions import Pattern

from data_pipeline import exons_introns_pipeline
from data_pipeline.constants import DATA_PATH
from data_pipeline.pipeline_lib import datasets, inputs as inputs_lib



def run(data_source_parameters: dict[str, dict[str, str | Pattern ]], input_parameters: dict[str, int]):
    """Runs dataset pipeline with provided data source and input parameters.

    Pipeline performs the following operations:
        - Creates inputs for datasets.
        - Validates input data.
        - Balances inputs across training, val and test datasets.
        - Writes datasets to csv files.
    """
    # INPUT parameters for data source and inputs
    #   -> build fragments with sequences and labels
    #       -> OUTPUT list[tuple[sequence: str, label:str]]
    inputs = inputs_lib.build(data_source_parameters, input_parameters)
    for label in inputs:
        print(f'Group {label}: {len(inputs[label])} inputs passed validation steps')

    # INPUT dict[str, list[str]]
    #   -> validate fragment output
    #       -> OUTPUT list[str (values separated by tabs)]
    validated_data = inputs_lib.validate(inputs, input_parameters["max_n_percentage"], input_parameters["length"])

    # INPUT dict[str, list[str]]
    # balance 1 and 0 inputs across train, test, val sets
    data_splits = inputs_lib.balance(validated_data)
    # WRITE TO FILE
    datasets.write_from_data_splits(data_splits, DATA_PATH, 'csv', ',', '\n')


def main():
    """Default pipeline sources sequences from exons and introns and writes csv files."""
    exons_introns_pipeline.run()


if __name__ == '__main__':
    main()



    
