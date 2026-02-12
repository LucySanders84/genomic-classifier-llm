import re

"""GFF files from http://www.candidagenome.org/download/gff/C_albicans_SC5314/Assembly22/ accessed on 2/11/2026 
FASTA files from http://www.candidagenome.org/download/sequence/C_albicans_SC5314/Assembly22/current/ 
 accessed on 2/11/2026"""

input_parameters_data_exons_and_introns = {
    'labels': {
        0: '0',
        1: '1'
    },
    'fsf': {
        0: 'C_albicans_SC5314_A22_current_intergenic.gff',
        1: 'C_albicans_SC5314_A22_current_features.gff'
    },
    'target': {
        0: 'intergenic regions',
        1: 'exons'
    },
    'ss': {
        'filename': 'C_albicans_SC5314_A22_current_chromosomes.fasta',
        'id_pattern': re.compile(r'Ca22chr\S+_C_albicans_SC5314')
    }

}


REF_SEQ_CDS_DATA = 'cds_from_genomic.fna'
REF_SEQ_CHROMOSOME_ID_PATTERN = r'(?<=locus_tag=\S+_C)\S'

CANDIDA_A_CURRENT_CHROMOSOMES_FASTA = 'C_albicans_SC5314_A22_current_chromosomes.fasta'
CANDIDA_A_ORFS_FASTA = 'C_albicans_SC5314_A22_current_orf_coding.fasta'
CANDIDA_A_ORFS_CHROMOSOME_ID_PATTERN = re.compile(r'(?<=COORDS:)Ca22chr\S+_C_albicans_SC5314')
CHROMOSOME_IDS = ['1', '2', '3', '4', '5', '6', '7', 'R']

CGD_CANDIDA_A_GENOME_GFF = 'C_albicans_SC5314_A22_current_features.gff'
CGD_EXON_TARGET_TYPE = 'exon'

CGD_CANDIDA_A_INTERGENIC_GFF = 'C_albicans_SC5314_A22_current_intergenic.gff'
CGD_INTRON_TARGET_TYPE = 'intergenic_region'

CGD_CANDIDA_A_A22_CHROMOSOME_ID_PATTERN = re.compile(r'Ca22chr\S+_C_albicans_SC5314')
GCA_CHROMOSOME_ID_PATTERN = r'(?<=chromosome\s)\S'
CODING_SEQUENCES_CSV = 'coding_sequences.csv'

GROUP_COUNT = 2
CONTIG_LENGTH = 512
STRIDE = int(CONTIG_LENGTH/2)





