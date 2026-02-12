import numpy
import numpy as np
from Bio.Seq import Seq
from Bio.Sequencing.Ace import Contig
from typing_extensions import Pattern

from classes.PipelineInputParameters import PipelineInputParameters
from constants import CGD_INTRON_TARGET_TYPE, CGD_EXON_TARGET_TYPE, CONTIG_LENGTH, STRIDE, GROUP_COUNT

from data_pipeline.lib import chromosome_dict
from data_pipeline.lib.contigs import short_contigs, contigs
from data_pipeline.lib.sequences import build_sequences

from constants import input_parameters_data_exons_and_introns as data




def main():


    #build contigs with sequences and labels -> OUTPUT list[tuple(sequence: str, label:str)
    #sequence source is CGD current chromosomes fasta
    chromosomes = chromosome_dict.build(
        data['ss']['filename'],
        data['ss']['id_pattern'])

    #build input parameters for input groups
    input_params = []
    for i in range(GROUP_COUNT - 1):
        input_params.append(
            PipelineInputParameters(
                label=data["labels"][i],
                sequence_source=chromosomes,
                feature_source_filename=data['fsf'][i],
                target_type=data['target'][i],
                contig_length=CONTIG_LENGTH,
                stride=STRIDE
        ))

    #get group sequences
    seq_lists = {}
    for params in input_params:
        seq_lists[params.label] = build_sequences.run(
                params.feature_source_filename,
                params.target_type,
                chromosomes)

    #build contigs
    contig_lists = {}
    for label in seq_lists.keys():
        for seq_list in seq_lists[label]:
            contig_lists[label] = contigs.get(seq_list, CONTIG_LENGTH, STRIDE)


    #build sequence/label tuples list


    #INPUT list[tuple(sequence: str, label:str)
    #   -> validate contig output
    #       -> OUTPUT list[str (values separated by tabs)]


    #INPUT list[str (values separated by tabs)]
    #   -> balance 1 and 0 inputs across training, test, dev sets
    #       -> WRITE TO FILE




    #coding_contigs = contigs.get(exons, CONTIG_LENGTH, STRIDE)
    #non_coding_contigs = contigs.get(introns, CONTIG_LENGTH, STRIDE)

    print(f'coding contigs: {len(coding_contigs)}')
    print(f'non-coding contigs: {len(non_coding_contigs)}')






    pass











if __name__ == '__main__':
    main()