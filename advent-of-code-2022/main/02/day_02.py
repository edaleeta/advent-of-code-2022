import enum
from typing import NamedTuple
"""
A, X = Rock
B, Y = Paper
C, Z = Scissors

Score determined by:
- shape selected
- outcome
"""


class Rules(NamedTuple):
    wins_against: str
    loses_against: str
    draws_against: str


rules_lookup = {
    "A": Rules(
        wins_against="Z",
        loses_against="Y",
        draws_against="X",
    ),
    "B": Rules(
        wins_against="X",
        loses_against="Z",
        draws_against="Y",
    ),
    "C": Rules(
        wins_against="Y",
        loses_against="X",
        draws_against="Z",
    ),
}

shape_to_points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def get_outcome_points(rules: Rules, my_shape: str) -> int:
    if my_shape in rules.wins_against:
        # loss
        return 0
    elif my_shape in rules.loses_against:
        # win
        return 6
    # draw
    return 3


def get_round_score(opponent_shape: str, my_shape: str) -> int:
    rules = rules_lookup[opponent_shape]
    shape_points = shape_to_points[my_shape]
    return shape_points + get_outcome_points(rules=rules, my_shape=my_shape)


def get_my_shape(opponent_shape, signal: str) -> str:
    rules = rules_lookup[opponent_shape]
    if signal == 'X':
        # lose against opponent
        return rules.wins_against
    if signal == 'Y':
        # draws against opponent
        return rules.draws_against
    # wins against opponent
    return rules.loses_against


class Mode(enum.Enum):
    PART_ONE = 1
    PART_TWO = 2


def parse_file(filename, mode=Mode.PART_ONE):
    total_points = 0
    with open(filename) as f:
        for line in f:
            shapes = line.strip().split()

            my_shape = get_my_shape(
                opponent_shape=shapes[0], signal=shapes[1]
            ) if mode == Mode.PART_TWO else shapes[1]

            total_points += get_round_score(shapes[0], my_shape)

    return total_points


print(get_round_score("A", "Y"))
print(get_round_score("B", "X"))
print(get_round_score("C", "Z"))

print(parse_file("sample.txt"))
print(parse_file("input.txt"))
print(parse_file("input.txt", mode=Mode.PART_TWO))
