import re

from typing_extensions import Pattern
from classes.SequenceBuilder import SequenceBuilder


def split_entries(file_contents: str) -> list[str]:
    return ['>' +entry.lstrip('>') for entry in re.split(r'\n>', file_contents.strip('\n'))]


def get_fasta_file_contents(filename):
    with open(filename) as f:
        return f.read()


def parse_to_sequences(fasta_seq_data_filename:str, chromosome_id_pattern: Pattern):
    return SequenceBuilder.build_from_fasta_entries(
        split_entries(
            get_fasta_file_contents(fasta_seq_data_filename)), chromosome_id_pattern)