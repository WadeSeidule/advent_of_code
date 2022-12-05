import helpers.utils as utils

lines = utils.input_lines('input.txt')

def split_range(input_range: str) -> tuple[int, int]:
    start, end = input_range.split('-')
    return int(start), int(end)

print(len(lines))

def part1() -> None:
    within = 0
    for line in lines:
        left, right = line.split(',')
        left_start, left_end = split_range(left)
        right_start, right_end = split_range(right)

        if left_start >= right_start and left_end <= right_end:
            within += 1
        elif right_start >= left_start and right_end <= left_end:
            within += 1

    print(within)


def part2() -> None:
    overlap = 0
    for line in lines:
        left, right = line.split(',')
        left_start, left_end = split_range(left)
        right_start, right_end = split_range(right)
        left_range = set(range(left_start, left_end + 1))
        right_range = set(range(right_start, right_end + 1))

        if len(left_range.intersection(right_range)) > 0:
            overlap += 1
    print(overlap)







if __name__ == "__main__":
    part1()
    part2()