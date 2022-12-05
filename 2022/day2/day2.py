from dataclasses import dataclass

from helpers import utils

lines = utils.input_lines('input.txt')

WIN_SCORE = 6
TIE_SCORE = 3

@dataclass
class Throw:
    name: str
    left: str
    right: str
    points: int
    beats: str
    loses: str

rock = Throw(
    name="ROCK",
    left="A",
    right="X",
    points=1,
    beats="SCISSORS",
    loses="PAPER"
)

paper = Throw(
    name="PAPER",
    left="B",
    right="Y",
    points=2,
    beats="ROCK",
    loses="SCISSORS"
)

scissors = Throw(
    name="SCISSORS",
    left="C",
    right="Z",
    points=3,
    beats="PAPER",
    loses="ROCK"
)


m = {
    "A": rock,
    "B": paper,
    "C": scissors,
    "X": rock,
    "Y": paper,
    "Z": scissors,
    "ROCK": rock,
    "PAPER": paper,
    "SCISSORS": scissors
}

def part1() -> None:
    score = 0
    for line in lines:
        left, right = line.split(' ')
        opponent, me = m[left], m[right]

        if me.beats == opponent.name:
            score += me.points + WIN_SCORE
        elif me.name == opponent.name:
            score += me.points + TIE_SCORE
        else:
            score += me.points
    print(score)


def part2() -> None:
    score = 0
    for line in lines:
        left, right = line.split(' ')
        opponent, me = m[left], m[right]

        if right == 'X': # need to lose
            score += m[opponent.beats].points
        elif right == 'Y': # need to tie
            score += opponent.points + TIE_SCORE
        elif right == "Z": # neet to win
            score += m[opponent.loses].points + WIN_SCORE
    print(score)



if __name__ == '__main__':
    part1()
    part2()