import os

def get_file_name(year: int, question: int, test: bool = False) -> str:

    test_str = 'test_' if test else ''

    file_name_one = f"{year}/question_{test_str}{question}_input.txt"
    file_name_two = f"{year}/{question}_{test_str}input.txt"

    if os.path.isfile(file_name_one):
        return file_name_one
    elif os.path.isfile(file_name_two):
        return file_name_two
    else:
        raise ValueError("file does not exist")

def get_puzzle_input_as_rows(year: int, question: int, test: bool = False):
    file_name = get_file_name(year, question, test=test)

    with open(file_name) as f:
        for row in f.readlines():
            yield row.strip()


def get_puzzle_input_as_string(year: int, question: int):

    file_name = get_file_name(year, question)

    with open(file_name) as f:
        return f.read()
