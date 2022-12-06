import pathlib

def input_lines(file: str) -> list[str]:
    with open(file) as f:
        return f.read().splitlines()

curr_dir = pathlib.Path(__file__).parent.resolve()
lines = input_lines(f'{curr_dir}/input.txt')

def part1() -> None:
    distinct_chars = 4
    datastream = lines[0]

    answer = None
    left_i = 0
    curr_chars: set[str] = set()
    for right_i, right in enumerate(datastream):
        if right_i - left_i < distinct_chars:
            if right in curr_chars: # restart
                left_i = right_i
                curr_chars = set()
        elif right_i - left_i == distinct_chars and len(curr_chars) == distinct_chars: # found
            answer = right_i - 1
            break

        curr_chars.add(right)

    print(answer)


def part2() -> None:
    distinct_chars = 14
    datastream = lines[0]

    answer = None
    left_i = 0
    curr_chars: set[str] = set()
    for right_i, right in enumerate(datastream):
        if right_i - left_i == distinct_chars - 1 : # found
            answer = right_i
            break

        if right_i - left_i < distinct_chars - 1:
            if right in curr_chars: # restart
                left_i = right_i
                curr_chars = set()

        curr_chars.add(right)

    print(answer)


if __name__ == "__main__":
    part1()
    part1_try()
    part2()