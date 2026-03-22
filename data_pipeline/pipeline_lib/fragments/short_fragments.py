from classes.Sequence import Sequence


def remove(seqs: list[Sequence], k: int) -> None:
    """
    Removes sequences shorter than k from sequence list.

    Args:
        seqs: list of DNA sequences
        k: minimum length
    """

    for seq in seqs[:]:
        if len(seq.bp_seq) < k:
            seqs.remove(seq)