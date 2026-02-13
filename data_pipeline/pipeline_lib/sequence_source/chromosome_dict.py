from typing_extensions import Pattern

from data_pipeline.pipeline_lib import fasta_file
from data_pipeline.constants import DATA_PATH

def get_data_filepath(current_dir):
    return current_dir


def build(fasta_filename: str, chromosome_id_pattern: Pattern):

    chromosomes = fasta_file.parse_to_sequences(
        DATA_PATH / fasta_filename,
        chromosome_id_pattern)
    chromosome_dict = {}
    for c in chromosomes:
        chromosome_dict[c.chromosome_id] = c
    return chromosome_dict