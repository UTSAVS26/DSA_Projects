import unittest
from src.utils import min_cash_flow, get_min_index, get_max_index, min_of_2

class TestUtils(unittest.TestCase):
    def test_min_cash_flow(self):
        graph = [
            [0, 1000, 2000],
            [0, 0, 5000],
            [0, 0, 0]
        ]
        self.assertEqual(min_cash_flow(graph), [3000, -4000, 1000])

    def test_get_min_index(self):
        self.assertEqual(get_min_index([3000, -4000, 1000]), 1)

    def test_get_max_index(self):
        self.assertEqual(get_max_index([3000, -4000, 1000]), 0)

    def test_min_of_2(self):
        self.assertEqual(min_of_2(3, 4), 3)
        self.assertEqual(min_of_2(5, 2), 2)

if __name__ == "__main__":
    unittest.main()