import re


def split_entries(file_contents: str) -> list[str]:
    return [entry.lstrip('>') for entry in re.split(r'\n>', file_contents.strip('\n'))]


def get_fasta_file_contents(filename):
    with open(filename) as f:
        return f.read()