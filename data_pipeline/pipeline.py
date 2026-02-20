
from typing_extensions import Pattern

from data_pipeline import exons_introns_pipeline
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
    print(f'{len(inputs)} inputs created from the following files:')
    for key in data_source_parameters["fsf"].keys():
        print("\t", data_source_parameters["fsf"][key])

    # INPUT list[tuple(sequence: str, label:str)
    #   -> validate fragment output
    #       -> OUTPUT list[str (values separated by tabs)]

    validated_inputs = inputs_lib.validate(inputs, input_parameters["max_n_percentage"], input_parameters["length"])
    print(f'{len(validated_inputs)} inputs created after validation steps')
    # INPUT list[str (values separated by tabs)]
    #   -> balance 1 and 0 inputs across train, test, val sets
    #       -> WRITE TO FILE

    pass

if __name__ == '__main__':
    #runs exons and introns pipeline as default
    exons_introns_pipeline.run()


    
