from classes.Sequence import Sequence


def remove(seqs: list[Sequence], k: int):
    for seq in seqs[:]:
        if len(seq.bp_seq) < k:
            seqs.remove(seq)