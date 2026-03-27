import re

from data_pipeline.constants import DATA_PATH
from data_pipeline.pipeline_lib import (
    sequence_source,
    sequences as seq_lib,
    inputs as inputs_lib,
    datasets)
from data_pipeline.pipeline_lib.data_source_parameters import EXONS_AND_INTRONS

def validate(inputs: dict[str, list[str]], max_n_percentage) -> dict[str,list[str]]:
    """Validates fragment length, alphabet, and a label presence to
    return a list of TSV-formatted strings.
    """
    validated_data = {}
    valid_dna_pattern = re.compile(r'^[ACGTN]+$', re.IGNORECASE)
    #check for missing labels or empty sequences
    for label in inputs:
        validated_data[label] = []
        for fragment in inputs[label]:
            if not label or not fragment:
                continue
            #ensure no weird characters from GFF/Fasta
            if not valid_dna_pattern.match(fragment):
                continue
            #drop sequences with mostly 'N' gaps
            n_count = fragment.upper().count('N')
            if (n_count / len(fragment)) > max_n_percentage:
                continue
            #if all pass, format as TSV string for the splitting step
            validated_data[label].append(fragment)

    return validated_data

def main():
    # get source sequences and set data source and input parameters
    data_source_params = EXONS_AND_INTRONS
    # get exons and intergenic regions
    chromosomes = sequence_source.build(
        data_source_params.sequence_source.filename,
        data_source_params.sequence_source.id_pattern)
    sequences = {}
    for key in data_source_params.labels:
        seq_objects = seq_lib.build(
            data_source_params.feature_source_filename[key],
            data_source_params.target_feature_type[key],
            chromosomes
        )
        sequences[key] = [seq.bp_seq for seq in seq_objects]

    # validate
    validated_sequences = validate(sequences, 0.02)

    # balance
    data_splits = inputs_lib.balance(validated_sequences)
    # WRITE TO FILE
    datasets.write_from_data_splits(data_splits, DATA_PATH / "low_preprocessing", 'csv', ',', '\n')

    pass

if __name__ == "__main__":
    main()