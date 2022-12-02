def get_puzzle_input_as_rows(year: int, question: int):
    with open(f"{year}/question_{question}_input.txt") as f:
        for row in f.readlines():
            yield row.strip()


def get_puzzle_input_as_string(year: int, question: int):
    with open(f"{year}/question_{question}_input.txt") as f:
        return f.read()
