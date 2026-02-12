import re

from typing_extensions import Pattern

from classes.Sequence import Sequence


class SequenceBuilder:

    @staticmethod
    def build_from_fasta_entry(entry: str, chromosome_id_pattern: Pattern):
        fasta = entry.split('\n')
        header = fasta[0]
        bp_seq = "".join(fasta[1:]).replace('\n', '').upper()
        m = re.search(chromosome_id_pattern, header)
        chromosome_id = m.group() if m is not None else None
        return Sequence(header, None, bp_seq=bp_seq, chromosome_id=chromosome_id)

    @staticmethod
    def build_from_fasta_entries(entries: list[str], chromosome_id_pattern: Pattern):
        return [SequenceBuilder.build_from_fasta_entry(entry, chromosome_id_pattern) for entry in entries]

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