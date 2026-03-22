import re

from typing_extensions import Pattern

from classes.Sequence import Sequence
from data_pipeline.pipeline_lib import fasta_file
from data_pipeline.constants import DATA_PATH


def build(fasta_filename: str, sequence_source_id_pattern: Pattern) -> dict[str, Sequence]:
    """Builds a list of sequences to use as a source for dataset inputs.

    Args:
        fasta_filename: name of file containing source data.
        sequence_source_id_pattern: the regex pattern for the desired id in the sequence source.

    Returns: data object containing key value pairs in which key is a sequence source id and
        value is a Sequence object.
    """

    sequence_source_list = fasta_file.parse_to_sequences(
        DATA_PATH / fasta_filename,
        sequence_source_id_pattern)
    sequence_sources = {}
    for seq in sequence_source_list:
        sequence_sources[seq.chromosome_id] = seq
    return sequence_sources
