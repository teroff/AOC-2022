from part1 import get_score, read_input
from part1_dict import get_total_score
import unittest


class TestPart1(unittest.TestCase):

    test_data = read_input('02_test.txt')

    def test_get_score(self):
        my_score = get_score(self.test_data)
        self.assertEqual(my_score, 15)

    def test_part1_dict(self):
        my_score = get_total_score(self.test_data)
        self.assertEqual(my_score, 15)