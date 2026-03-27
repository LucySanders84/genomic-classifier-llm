import re

from classes.DataSourceParameters import DataSourceParameters
from classes.SequenceSourceData import SequenceSourceData
from data_pipeline.constants import DATA_PATH

EXONS_AND_INTRONS = DataSourceParameters(
    {
        '0': '0',
        '1': '1'
    },
    {
        '0': DATA_PATH / 'C_albicans_SC5314_A22_current_intergenic.gff',
        '1': DATA_PATH / 'C_albicans_SC5314_A22_current_features.gff'
    },
    {
        '0': 'intergenic_region',
        '1': 'exon'
    },
    SequenceSourceData(
        DATA_PATH / 'C_albicans_SC5314_A22_current_chromosomes.fasta',
        re.compile(r'Ca22chr\S+_C_albicans_SC5314'))
)