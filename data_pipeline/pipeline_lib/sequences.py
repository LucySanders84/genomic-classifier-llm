from classes.Sequence import Sequence
from classes.SequenceBuilder import SequenceBuilder


def build_from_gff(gff_filename: str, target_fragment_type: str):
    with open(gff_filename) as gff:
        gff_file_contents = gff.read()
        seqs = SequenceBuilder.build_from_gff(
            gff_file_contents,
            target_fragment_type)
    return seqs


def build(
        filename: str,
        target_fragment_type: str,
        sequence_source: dict[str, Sequence],
        source_type='chromosome',
        file_format='gff'):
    try:
        if file_format != 'gff' and file_format != 'gff3':
            raise ValueError('Only gff or gff3 formats supported')

        if source_type != 'chromosome':
            raise ValueError('Only chromosome source type supported')

        seqs = build_from_gff(filename, target_fragment_type)
        set_all_seqs_by_chromosome_loci(sequence_source, seqs)
        return seqs

    except ValueError as e:
        print(f'ValueError raised: {e}')


def get_bp_seqs_from_chromosome_loci(seq: Sequence, chromosome: Sequence):
    [start, stop] = seq.chromosome_loci
    return chromosome.bp_seq[start - 1: stop]


def set_all_seqs_by_chromosome_loci(chromosomes: dict[str, Sequence], seqs: list[Sequence]):
    for seq in seqs:
        chromosome = chromosomes[seq.chromosome_id]
        seq.bp_seq = get_bp_seqs_from_chromosome_loci(seq, chromosome)