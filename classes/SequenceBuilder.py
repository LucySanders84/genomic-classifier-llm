import re

from classes.Sequence import Sequence


class SequenceBuilder:

    @staticmethod
    def build_from_fasta_entry(entry: str):
        fasta = entry.split('\n')
        header = fasta[0]
        bp_seq = "".join(fasta[1:]).replace('\n', '').upper()
        genome_location = None
        read_direction = 'forward'
        m = re.search(r'location=', header)
        if m is not None:
            complement = re.search(r'complement', header[m.start():])
            read_direction = 'complement' if complement is not None else 'forward'
            location = re.search(r'(?<=>)\S*', header[m.start():])
            genome_location = location if location is not None else None
        return Sequence(header, bp_seq, read_direction, genome_location)

    @staticmethod
    def build_from_fasta_entries(entries: list[str]):
        return [SequenceBuilder.build_from_fasta_entry(entry) for entry in entries]

    @staticmethod
    def build_from_gff_line(entry: str):
        [seq_name, _, _, start, end, _, strand, _, attribute] = entry.split('\t')
        chromosome_loci = [int(start), int(end)]
        return Sequence(attribute, strand, chromosome_id=seq_name, chromosome_loci=chromosome_loci)

    @staticmethod
    def build_from_gff(gff_file_contents:str, target_contig_type: str):
        lines = []
        for line in gff_file_contents.strip('\n').split('\n'):
            if re.search(rf'\t{target_contig_type}\t', line):
                lines.append(line)
        return [SequenceBuilder.build_from_gff_line(line) for line in lines]