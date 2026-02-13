from typing_extensions import Pattern

from classes.PipelineParameters import PipelineParameters

from data_pipeline.pipeline_lib.sequence_source import chromosome_dict
from data_pipeline.pipeline_lib.contigs import contigs
from data_pipeline.pipeline_lib.sequences import build_sequences

"""
definitions:
input - a line item in a dataset used to train LLM
sequence - a string of base pairs
contig - a sequence split from a larger sequence
"""

def run(data_source_parameters: dict[str, dict[str, str | Pattern ]], input_parameters: dict[str, int]):

    # build contigs with sequences and labels -> OUTPUT list[tuple(sequence: str, label:str)

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
                contig_length=input_parameters['length'],
                stride=input_parameters['stride']
            ))

    # get sequences for each group
    seq_lists = {}
    for params in pipeline_params:
        seq_lists[params.label] = build_sequences.run(
            params.feature_source_filename,
            params.target_type,
            chromosomes)

    # build contigs
    contig_lists = {}
    for key in seq_lists.keys():
        contig_lists[key] = contigs.build(seq_lists[key], input_parameters['length'], input_parameters['stride'])

    # build sequence/label tuples list
    inputs: list[tuple] = []
    for label in contig_lists.keys():
        for contig in contig_lists[label]:
            inputs.append(tuple([contig, label]))
    pass

    # INPUT list[tuple(sequence: str, label:str)
    #   -> validate contig output
    #       -> OUTPUT list[str (values separated by tabs)]

    # INPUT list[str (values separated by tabs)]
    #   -> balance 1 and 0 inputs across train, test, val sets
    #       -> WRITE TO FILE
    pass