
from classes.Sequence import Sequence
from data_pipeline.pipeline_lib.fragments import short_fragments


def get(seqs:list[Sequence], k:int, t:int):
    return [fragment for seq in seqs for fragment in seq.get_kmers(k, t)]


def build(seq_list: list[Sequence], fragment_length: int, stride: int, remove_short_fragments=True):
    if remove_short_fragments is True:
        short_fragments.remove(seq_list, fragment_length)
    return get(seq_list, fragment_length, stride)


