from enum import Enum, auto


class Shape(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


shape_from_letter = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS,
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSORS
}

shape_value: dict[Shape, int] = {
    Shape.ROCK: 1,
    Shape.PAPER: 2,
    Shape.SCISSORS: 3
}

first_player_wins = {
    (Shape.ROCK, Shape.SCISSORS),
    (Shape.PAPER, Shape.ROCK),
    (Shape.SCISSORS, Shape.PAPER)
}


def get_score_first_player(shape1: Shape, shape2: Shape) -> int:
    if (shape1, shape2) in first_player_wins:
        return 6
    if shape1 == shape2:
        return 3
    else:
        return 0


def read_input(file) -> list:
    with open(file, 'r') as f:
        return f.read().splitlines()


def get_round_score(elf_shape: Shape, my_shape: Shape) -> int:
    shape_score = shape_value[my_shape]
    outcome_score = get_score_first_player(my_shape, elf_shape)
    return shape_score + outcome_score


def get_score(lines) -> int:
    score = 0
    for line in lines:
        elf_shape = shape_from_letter[line[0]]
        my_shape = shape_from_letter[line[-1]]
        score += get_round_score(elf_shape, my_shape)

    return score


if __name__ == '__main__':
    lines = read_input('02.txt')
    my_score = get_score(lines)

    print(my_score)

