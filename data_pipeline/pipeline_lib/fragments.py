"""Module containing fragment related functions."""
from classes.Sequence import Sequence


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
        remove_short_fragments(seq_list, fragment_length)
    return get(seq_list, fragment_length, stride)


def remove_short_fragments(seqs: list[Sequence], k: int) -> None:
    """
    Removes sequences shorter than k from sequence list.

    Args:
        seqs: list of DNA sequences
        k: minimum length
    """

    for seq in seqs[:]:
        if len(seq.bp_seq) < k:
            seqs.remove(seq)





