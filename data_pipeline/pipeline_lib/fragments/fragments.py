from classes.Sequence import Sequence
from data_pipeline.pipeline_lib.fragments import short_fragments


def get(seqs:list[Sequence], k:int, t:int) -> list[str]:
    """Creates fragments of k length with stride of t from a list of sequences."""

    return [fragment for seq in seqs for fragment in seq.get_kmers(k, t)]


def build(seq_list: list[Sequence], fragment_length: int, stride: int, remove_short_seqs: bool = True) -> list[str]:
    """Builds a list of fragments from a list of sequences.

    If remove_short_seqs is true, sequences shorter than fragment length are removed before fragmentation.

    Args:
        seq_list: list of DNA sequences
        fragment_length: desired length of fragments
        stride: number of base pairs to move sliding window for each fragmentation
        remove_short_seqs (optional): removes sequences shorter than fragment length before fragmentation. Defaults to True.

    """

    if remove_short_seqs is True:
        short_fragments.remove(seq_list, fragment_length)
    return get(seq_list, fragment_length, stride)





