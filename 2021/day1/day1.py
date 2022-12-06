import pathlib
from pprint import pprint

def input_lines(file: str) -> list[str]:
    with open(file) as f:
        return f.read().splitlines()

curr_dir = pathlib.Path(__file__).parent.resolve()
lines = input_lines(f'{curr_dir}/input.txt')

def part1() -> None:
    count = 0
    for i, line in enumerate(lines):
        if i < len(lines) - 1 and int(lines[i+1]) > int(line):
            count += 1

    print(count)


def part2() -> None:
    pass


if __name__ == "__main__":
    part1()
    part2()