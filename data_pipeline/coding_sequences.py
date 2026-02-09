import re
from dataclasses import dataclass

from constants import CODING_SEQ_DATA, CODING_SEQUENCES_CSV, LABEL_FOR_CODING_SEQUENCES
from fasta_file import get_fasta_file_contents, split_entries
from data_pipeline.Sequence import Sequence


def add_sequence_to_csv(seq, label, file):
    file.write(f'{seq},{label}\n')


def run(fasta_seq_data_filename, csv_filename, label):
    #open destination (csv file)
    with open(csv_filename, 'w') as f:
        #add 'sequence,label' as headers in first row
        f.write('sequence,label\n')
        #split fasta file into entries, for each entry in fasta file, write bp sequence and label to destination csv file
        for seq in Sequence.build_from_fasta_entries(split_entries(get_fasta_file_contents(fasta_seq_data_filename))):
            add_sequence_to_csv(seq.bp_seq, label, f)
    pass


def main():
    run(CODING_SEQ_DATA, CODING_SEQUENCES_CSV, LABEL_FOR_CODING_SEQUENCES)


if __name__ == '__main__':
    main()