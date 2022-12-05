import helpers.utils as utils

lines = utils.input_lines('input.txt')

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_points(letter: str) -> int:
    return LETTERS.index(letter) + 1

def part1() -> None:
    points = 0
    for line in lines:
        middle = len(line)//2
        left, right = line[:middle], line[middle:]
        shared = set(left).intersection(set(right))
        points += sum(get_points(item) for item in shared)

    print(points)

def part2() -> None:
    points = 0
    for line in zip(*[iter(lines)] * 3):
        sets = [set(l) for l in line]
        badge = set.intersection(*sets).pop()
        points += get_points(badge)

    print(points)

if __name__ == '__main__':
    part1()
    part2()
