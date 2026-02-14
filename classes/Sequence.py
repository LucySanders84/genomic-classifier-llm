import re


class Sequence:
    header: str
    bp_seq: str
    genome_loci: list[str]
    chromosome_id: str = None
    read_direction: str
    chromosome_loci: list[int]


    def __init__(self, header, read_direction, bp_seq=None, genome_loci=None, label=None, chromosome_id=None, chromosome_loci=None):
        self.header = header
        self.bp_seq = bp_seq
        self.label = label
        self.genome_loci = genome_loci
        self.read_direction = read_direction
        self.chromosome_id = chromosome_id
        self.chromosome_loci = chromosome_loci

    def set_label(self, label):
        self.label = label

    def set_chromosome_id(self, chromosome: str):
        self.chromosome_id = chromosome

    def get_kmers(self, k: int, t:int, add_downstream_short_fragments=True):
        kmers = []
        i = 0
        l = len(self.bp_seq)
        while i < l - k + 1:
            kmers.append(self.bp_seq[i:i+k])
            i += t
        if l - i < k:
            if add_downstream_short_fragments is True:
                bp_count_to_add = k - (l - i)
                kmers.append(self.bp_seq[i - bp_count_to_add:])
            else:
                kmers.append(self.bp_seq[i:])
        return kmers


def main():
    pass