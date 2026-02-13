
from classes.Sequence import Sequence
from data_pipeline.pipeline_lib.contigs import short_contigs


def get(seqs:list[Sequence], k:int, t:int):
    return [contig for seq in seqs for contig in seq.get_kmers(k, t)]


def build(seq_list: list[Sequence], contig_length: int, stride: int, remove_short_contigs=True):
    if remove_short_contigs is True:
        short_contigs.remove(seq_list, contig_length)
    return get(seq_list, contig_length, stride)


