import regex as re

from classes.Sequence import Sequence


def find_chromosome_id(seq:Sequence, valid_ids, pattern):
    m = re.search(pattern, seq.header)
    if m is not None:
        chromosome_id = m.group(0)
        if chromosome_id not in valid_ids:
            print('chromosome id not valid', chromosome_id)
        return chromosome_id
    else:
        return None