shape = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

shape_score = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

win_moves = {
    ("Rock",  "Scissors"),
    ("Paper", "Rock"),
    ("Scissors", "Paper")
}


def read_input(file) -> list:
    with open(file, 'r') as f:
        return f.read().splitlines()


def get_move_score(shape1: str, shape2: str) -> int:
    if (shape1, shape2) in win_moves:
        return 6
    if shape1 == shape2:
        return 3
    else:
        return 0


def get_round_score(elf: str, me: str) -> int:
    my_move_score = shape_score[me]
    move_score = get_move_score(me, elf)
    return my_move_score + move_score


def get_total_score(data: list) -> int:
    result = 0
    for index, move in enumerate(data):
        elf, me = move.split()
        elf = shape[elf]
        me = shape[me]
        score = get_round_score(elf, me)
        result += score
    return result


if __name__ == '__main__':
    game_data = read_input('02.txt')
    print(get_total_score(game_data))
