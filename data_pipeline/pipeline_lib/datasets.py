import os

def format_inputs_for_dataset(data: list[tuple[str, str]], line_delimiter, col_delimiter, output_format='list'):
    try:
        if output_format == 'list':
            return col_delimiter.join([line_delimiter.join(line) for line in data])
        else:
            raise ValueError('Only output format of "list" is currently supported.')
    except ValueError as e:
        print(e)


def write_from_data_splits(data_splits: dict[str, list[tuple[str,str]]], output_dir, file_extension: str, line_delimiter:str, col_delimiter: str):
    # This writes to file system
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename, data in data_splits.items():

        path = os.path.join(output_dir, filename + '.' + file_extension)

        formatted_data = format_inputs_for_dataset(data, line_delimiter, col_delimiter)
        with open(path, 'w') as f:
            f.writelines(formatted_data)
        print(f"Successfully created {len(data)} with training data sequences to {path}")