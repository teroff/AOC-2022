def build_2d_array_from_file(file) -> list:
    """
    Decided to build a 2D array from the source file so that we can reuse it later should we want to do anything else
    with this information, like find the top x of elfs with the most calories
    :param file:
    :return: 2D array of elfs and their calories [[], [], []]
    """
    result = []
    it = enumerate(open(file, 'r'))
    elf = []
    while True:
        try:
            index, line = next(it)
            line = line.strip()
            if not line == "":
                elf.append(int(line))
            else:
                result.append(elf)
                elf = []
        except StopIteration:
            result.append(elf)
            break

    return result


def get_elfs_calories_object(file) -> map:
    """
    This is another implementation but with using maps instead of 2D arrays because they are faster and we can do
    more stuff with an object
    :param file:
    :return: {int: list}
    """
    it = enumerate(open(file, 'r'))
    result = {}
    calories = []
    i = 0
    while True:
        try:
            index, line = next(it)
            line = line.strip()
            if not line == "":
                calories.append(int(line))
            else:
                result[i] = calories
                i += 1
                calories = []
        except StopIteration:
            result[i] = calories
            break

    return result


def get_sum_of_top_n_elfs(calories_list: list, n: int) -> int:
    """
    Here we are taking a 2D array of the elfs and their calories, and the n number of elf we would like to get the
    data from. And we are returning the sum of n elfs' calories.
    :param calories_list:
    :param n: int
    :return: int sum of the calories from the n elfs
    """
    array_of_x = sorted(calories_list, key=sum, reverse=True)
    return sum([sum(x) for x in array_of_x[0:n]])


if __name__ == '__main__':
    print(f"The top Elf carries {get_sum_of_top_n_elfs(build_2d_array_from_file('01.txt'), 1)} calories")
    print(f"The top three Elves carry {get_sum_of_top_n_elfs(build_2d_array_from_file('01.txt'), 3)} calories")
