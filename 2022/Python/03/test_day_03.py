from part1 import count_the_priorities, read_data
from part2 import get_rucksacks_priorities, split_into_groups
import unittest


class TestDay03(unittest.TestCase):

    def test_part1_solution(self):
        data = read_data("day03_test.txt")
        result = count_the_priorities(data)

        self.assertEqual(result, 157)

    def test_part2_solution(self):
        data = split_into_groups(read_data('day03_test.txt'), 3)
        result = get_rucksacks_priorities(data)

        self.assertEqual(result, 70)