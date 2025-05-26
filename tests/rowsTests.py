import unittest
import pandas as pd

class TestCSVRows(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('profiles1.csv')

    def test_has_minimum_900_rows(self):
        self.assertGreaterEqual(self.df.shape[0], 900, "Expected at least 900 rows")

    def test_not_less_than_900_rows(self):
        self.assertFalse(self.df.shape[0] < 900, "Too few rows")

if __name__ == '__main__':
    unittest.main()