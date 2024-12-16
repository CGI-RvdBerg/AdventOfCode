import unittest
from tkinter.messagebox import IGNORE

from Day12.GardenGroups import do_part_1


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """
        Common setup for the tests, if needed in the future.
        Currently, this is just a placeholder.
        """
        pass

    def test_example1(self):
        input_data = """AAAA
BBCD
BBCC
EEEC"""
        # Verify the output matches the expected value for the given input
        self.assertEqual(do_part_1(input_data), 140)

    def test_example2(self):
        input_data = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
        # Verify the output matches the expected value for the given input
        self.assertEqual(do_part_1(input_data), 772)

    def test_example3(self):
        input_data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
        # Verify the output matches the expected value for the given input
        self.assertEqual(do_part_1(input_data), 1930)


if __name__ == '__main__':
    unittest.main()
