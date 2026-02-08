import re
from dataclasses import dataclass

LABEL_FOR_CODING_SEQUENCES = 1
CODING_SEQ_DATA = 'cds_from_genomic.fna'
CODING_SEQUENCES_CSV = 'coding_sequences.csv'


def add_sequence_to_csv(seq, label, file):
    file.write(f'{seq},{label}\n')


def get_fasta_file_contents(filename):
    with open(filename) as f:
        return f.read()


@dataclass
class FastaSeq:
    header: str
    seq: str


def get_fasta_seqs(file_content) -> list[FastaSeq]:
    fasta_seqs = []
    for fasta in re.split(r'\n>', file_content.strip('\n')):
        fasta = fasta.split('\n')
        fasta_seqs.append(FastaSeq(header=fasta[0], seq="".join(fasta[1:]).replace('\n', '')))
    return fasta_seqs


def run(fasta_seq_data_filename, csv_filename, label):
    fasta_seqs = get_fasta_seqs(get_fasta_file_contents(fasta_seq_data_filename))
    with open(csv_filename, 'w') as f:
        f.write('sequence,label\n')
        for fasta_seq in fasta_seqs:
            add_sequence_to_csv(fasta_seq.seq, label, f)
    pass


def main():
    run(CODING_SEQ_DATA, CODING_SEQUENCES_CSV, LABEL_FOR_CODING_SEQUENCES)


if __name__ == '__main__':
    main()