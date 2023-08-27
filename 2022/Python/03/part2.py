from part1 import AlPHABET


def get_data(file) -> list:
    with open(file, 'r') as f:
        return f.read().splitlines()


def split_into_groups(data: list, group_size: int) -> list:
    result = []
    while len(data) > group_size:
        result.append(data[:group_size])
        data = data[group_size:]
    result.append(data)
    return result


def get_rucksacks_priorities(data: list) -> int:
    result = 0
    for group in data:
        badge = set(group[0]).intersection(group[1]).intersection(group[-1])
        for letter in badge:
            result += AlPHABET.index(letter)+1

    return result


if __name__ == '__main__':
    data_from_file = get_data('day03_data.txt')
    groups_data = split_into_groups(data_from_file, 3)
    print(get_rucksacks_priorities(groups_data))