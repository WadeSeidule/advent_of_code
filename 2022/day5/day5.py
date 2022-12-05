import pathlib
import collections
from pprint import pprint

def input_lines(file: str) -> list[str]:
    with open(file) as f:
        return f.read().splitlines()

curr_dir = pathlib.Path(__file__).parent.resolve()
lines = input_lines(f'{curr_dir}/input.txt')

def parse_verticle_lines() -> tuple[list[list[str]], int]:
    parsed_lines: list[list[str]] = []
    for i, line in enumerate(lines):
        if line == '':
            return parsed_lines, i

        curr_i, curr_chars, item_list = 1, [], []
        for char in line:
            if curr_i < 4:
                curr_chars.append(char)
                curr_i += 1
            elif curr_i == 4:
                curr_i = 1
                item_list.append("".join(curr_chars))
                curr_chars = []
        # append last three
        item_list.append("".join(curr_chars))

        parsed_lines.append(item_list)

    raise Exception("Did not parse correctly if got here")


def build_stacks(parsed_lines: list[list[str]]) -> dict[str, list[str]]:
    stacks = collections.defaultdict(list)
    for line in reversed(parsed_lines[:-1]):
        for i, item in enumerate(line):
            if item.strip() == "":
                continue
            stacks[str(i+1)].append(item)
    return stacks


def part1() -> None:
    plines, end_index = parse_verticle_lines()
    stacks = build_stacks(plines)
    command_lines = lines[end_index + 1:]

    for cmd in command_lines:
        cmd_parts = [p for p in cmd.split(' ') if p.isdigit()]
        quantity, start_stack, end_stack = cmd_parts
        for _ in range(int(quantity)):
            item_to_move = stacks[start_stack].pop()
            stacks[end_stack].append(item_to_move)

    result = "".join([item[-1] for item in stacks.values()])

    print(result.replace("[", "").replace("]", ""))


def part2() -> None:
    plines, end_index = parse_verticle_lines()
    stacks = build_stacks(plines)
    command_lines = lines[end_index + 1:]

    for cmd in command_lines:
        cmd_parts = [p for p in cmd.split(' ') if p.isdigit()]
        quantity, start_stack, end_stack = cmd_parts
        items_left = stacks[start_stack][:-int(quantity)]
        items_to_move = stacks[start_stack][-int(quantity):]
        stacks[start_stack] = items_left
        stacks[end_stack].extend(items_to_move)

    result = "".join([item[-1] for item in stacks.values()])

    print(result.replace("[", "").replace("]", ""))


if __name__ == "__main__":
    part1()
    part2()