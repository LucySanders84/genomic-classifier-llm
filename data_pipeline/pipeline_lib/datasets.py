"""Module containing dataset functions."""

import os

def format_inputs_for_dataset(data: list[tuple[str, str]], line_delimiter, col_delimiter, output_format='list'):
    """Formats inputs for dataset.

    Only output format currently supported is a list. If a different value for is provided for the
    output_format parameter a value error is raised.

    Args:
        data: input data.
        line_delimiter: the value that delimits lines in the input data.
        col_delimiter: the value that delimits columns in the input data.
        output_format (optional): defaults to "list".
    """
    try:
        if output_format == 'list':
            return col_delimiter.join([line_delimiter.join(line) for line in data])
        else:
            raise ValueError('Only output format of "list" is currently supported.')
    except ValueError as e:
        print(e)


def write_from_data_splits(data_splits: dict[str, list[tuple[str,str]]], output_dir, file_extension: str, line_delimiter:str, col_delimiter: str) -> None:
    """Writes from data object containing split datasets to file.

    Args:
        data_splits: key = dataset name, value = list of sequence/label tuples.
        output_dir: directory to which files are written.
        file_extension: desired file extension
        line_delimiter: value with which to delimit lines in the output file.
        col_delimiter: value with which to delimit columns in the output file.
    """

    # This writes to file system
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename, data in data_splits.items():

        path = os.path.join(output_dir, filename + '.' + file_extension)

        formatted_data = format_inputs_for_dataset(data, line_delimiter, col_delimiter)
        with open(path, 'w') as f:
            f.write(f'sequence{line_delimiter}label{col_delimiter}')
            f.writelines(formatted_data)
        print(f"Successfully created {len(data)} with training data sequences to {path}")