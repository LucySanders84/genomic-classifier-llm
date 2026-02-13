from classes.Sequence import Sequence
from data_pipeline.pipeline_lib.sequences import get_bp_sequence


def by_chromosome_loci(chromosomes: dict[str, Sequence], seqs: list[Sequence]):
    for seq in seqs:
        chromosome = chromosomes[seq.chromosome_id]
        seq.bp_seq = get_bp_sequence.from_chromosome_loci(seq, chromosome)