from classes.Sequence import Sequence
from classes.SequenceBuilder import SequenceBuilder
from data_pipeline.pipeline_lib.sequences import set_all_sequences


def from_gff(gff_filename: str,target_contig_type: str):
    with open(gff_filename) as gff:
        gff_file_contents = gff.read()
        seqs = SequenceBuilder.build_from_gff(
            gff_file_contents,
            target_contig_type)
    return seqs


def run(
        filename: str,
        target_contig_type: str,
        sequence_source: dict[str, Sequence],
        source_type='chromosome',
        file_format='gff'):
    try:
        if file_format != 'gff' and file_format != 'gff3':
            raise ValueError('Only gff or gff3 formats supported')

        if source_type != 'chromosome':
            raise ValueError('Only chromosome source type supported')

        seqs = from_gff(filename, target_contig_type)
        set_all_sequences.by_chromosome_loci(sequence_source, seqs)
        return seqs

    except ValueError as e:
        print(f'ValueError raised: {e}')
