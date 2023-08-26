GAME_MOVES = {
    "A": {
        "newRules": {
            "X": 3,
            "Y": 4,
            "Z": 8
        },
        "regularRules": {
            "X": 4,
            "Y": 8,
            "Z": 3
        }
    },
    "B": {
        "newRules": {
            "X": 1,
            "Y": 5,
            "Z": 9
        },
        "regularRules": {
            "X": 1,
            "Y": 5,
            "Z": 9
        }
    },
    "C": {
        "newRules": {
            "X": 2,
            "Y": 6,
            "Z": 7
        },
        "regularRules": {
            "X": 7,
            "Y": 2,
            "Z": 6
        }
    }
}


def count_points(tournament_data, rigged):
    points = 0
    for index, tournament_data in enumerate(tournament_data):
        opponent, me = tournament_data.split()
        points += GAME_MOVES[opponent][rigged][me]

    return points


def get_tournament_data(file):
    with open(file, 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    input_data = get_tournament_data('02.txt')
    print(f"Total Points using regular rules:\t", count_points(input_data, "regularRules"))
    print(f"Total Points with the new rules:\t", count_points(input_data, "newRules"))
