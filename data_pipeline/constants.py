import re

from pathlib import Path
"""
data source:
GFF files from http://www.candidagenome.org/download/gff/C_albicans_SC5314/Assembly22/ accessed on 2/11/2026 
FASTA files from http://www.candidagenome.org/download/sequence/C_albicans_SC5314/Assembly22/current/ accessed on 2/11/2026

definitions:
input - a line item in a dataset used to train LLM
sequence - a string of base pairs
contig - a sequence split from a larger sequence
 """


ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = ROOT_DIR / 'data_files'

CONTIG_LENGTH = 512

DATA_SOURCE_PARAMETERS_EXONS_AND_INTRONS = {
    'labels': {
        '0': '0',
        '1': '1'
    },
    'fsf': {
        '0': DATA_PATH / 'C_albicans_SC5314_A22_current_intergenic.gff',
        '1': DATA_PATH / 'C_albicans_SC5314_A22_current_features.gff'
    },
    'target': {
        '0': 'intergenic_region',
        '1': 'exon'
    },
    'ss': {
        'filename': DATA_PATH / 'C_albicans_SC5314_A22_current_chromosomes.fasta',
        'id_pattern': re.compile(r'Ca22chr\S+_C_albicans_SC5314')
    }
}

INPUT_PARAMETERS_EXONS_AND_INTRONS = {
    'length': CONTIG_LENGTH,
    'stride': int(CONTIG_LENGTH/2)
}







