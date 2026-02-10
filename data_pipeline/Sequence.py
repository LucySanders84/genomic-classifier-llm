import re


class Sequence:
    header: str
    bp_seq: str
    genome_loci: list[str]
    chromosome_id: str = None
    read_direction: str


    def __init__(self, header, bp_seq, read_direction, genome_location=None, label=None):
        self.header = header
        self.bp_seq = bp_seq
        self.label = label
        self.genome_loci = genome_location
        self.read_direction = read_direction

    def set_label(self, label):
        self.label = label

    def set_chromosome_id(self, chromosome: str):
        self.chromosome_id = chromosome

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
            location = re.findall(r'\d+..\d+', header[m.start():])
            genome_location = location if location is not None else None
        return Sequence(header, bp_seq, read_direction, genome_location)

    @staticmethod
    def build_from_fasta_entries(entries: list[str]):
        return [Sequence.build_from_fasta_entry(entry) for entry in entries]


def main():
    pass