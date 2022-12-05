import pathlib

def input_lines(file: str) -> list[str]:
    with open(file) as f:
        return f.read().splitlines()

curr_dir = pathlib.Path(__file__).parent.resolve()
lines = input_lines(f'{curr_dir}/input.txt')

def part1() -> None:
    pass


def part2() -> None:
    pass


if __name__ == "__main__":
    part1()
    part2()