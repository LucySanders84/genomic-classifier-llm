from data_pipeline.constants import DATA_SOURCE_PARAMETERS_EXONS_AND_INTRONS, INPUT_PARAMETERS_EXONS_AND_INTRONS
from data_pipeline import pipeline


def run():
    pipeline.run(
        DATA_SOURCE_PARAMETERS_EXONS_AND_INTRONS,
        INPUT_PARAMETERS_EXONS_AND_INTRONS)