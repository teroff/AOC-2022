import string

AlPHABET = string.ascii_letters


def get_two_parts(n: str) -> str:
    half_n = int(len(n)/2)

    return [n[:half_n], n[half_n:]]


def get_intersection(part1, part2):
    return list(set(part1).intersection(part2))


def read_data(file) -> list:
    with open(file, 'r') as f:
        return f.read().splitlines()


def count_the_priorities(data) -> int:
    result = 0
    for line in data:
        part1, part2 = get_two_parts(line)
        intersection = get_intersection(part1, part2)

        for letter in intersection:
            result += AlPHABET.index(letter)+1

    return result


if __name__ == '__main__':
    data = read_data('day03_data.txt')
    result = count_the_priorities(data)
    print(result)