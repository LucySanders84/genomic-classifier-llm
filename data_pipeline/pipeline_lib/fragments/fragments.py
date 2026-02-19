import re

from classes.Sequence import Sequence
from data_pipeline.pipeline_lib.fragments import short_fragments


def get(seqs:list[Sequence], k:int, t:int) -> list[str]:
    return [fragment for seq in seqs for fragment in seq.get_kmers(k, t)]


def build(seq_list: list[Sequence], fragment_length: int, stride: int, remove_short_fragments=True) -> list[str]:
    if remove_short_fragments is True:
        short_fragments.remove(seq_list, fragment_length)
    return get(seq_list, fragment_length, stride)


def validate(inputs: list[tuple[str, str]], max_n_percentage, expected_length) -> list[str]:
    """Validates fragment length, alphabet, and a label presence to
    return a list of TSV-formatted strings.
    """
    validated_data = []
    valid_dna_pattern = re.compile(r'^[ACGTN]+$', re.IGNORECASE)
    #check for missing labels or empty sequences
    for fragment, label in inputs:
        if not label or not fragment:
            continue
        #length from constants.py
        if len(fragment) != expected_length:
            continue
        #ensure no weird characters from GFF/Fasta
        if not valid_dna_pattern.match(fragment):
            continue
        #drop sequences with mostly 'N' gaps
        n_count = fragment.upper().count('N')
        if (n_count / expected_length) > max_n_percentage:
            continue
        #if all pass, format as TSV string for the splitting step
        validated_data.append(f"{fragment}\t{label}\n")

    return validated_data


