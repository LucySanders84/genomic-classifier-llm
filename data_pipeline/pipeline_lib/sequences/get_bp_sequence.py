from classes.Sequence import Sequence


def from_chromosome_loci(seq: Sequence, chromosome: Sequence):
    [start, stop] = seq.chromosome_loci
    return chromosome.bp_seq[start - 1: stop]