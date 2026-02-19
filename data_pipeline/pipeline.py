
from typing_extensions import Pattern

from data_pipeline.pipeline_lib.fragments import fragments
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

    # INPUT list[tuple(sequence: str, label:str)
    #   -> validate fragment output
    #       -> OUTPUT list[str (values separated by tabs)]

    validated_inputs = fragments.validate(inputs, input_parameters["max_n_percentage"], input_parameters["length"])

    # INPUT list[str (values separated by tabs)]
    #   -> balance 1 and 0 inputs across train, test, val sets
    #       -> WRITE TO FILE

    pass


    
