"""Module containing exons and introns pipeline"""

from data_pipeline.constants import DATA_SOURCE_PARAMETERS_EXONS_AND_INTRONS, INPUT_PARAMETERS_EXONS_AND_INTRONS
from data_pipeline import pipeline


def run():
    """Runs pipeline using exon and intron data source and input parameters from constants module."""
    pipeline.run(
        DATA_SOURCE_PARAMETERS_EXONS_AND_INTRONS,
        INPUT_PARAMETERS_EXONS_AND_INTRONS)