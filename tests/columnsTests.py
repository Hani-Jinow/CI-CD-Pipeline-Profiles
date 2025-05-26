import unittest
import pandas as pd

class TestCSVColumns(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('profiles1.csv')

    def test_has_12_columns(self):
        self.assertEqual(self.df.shape[1], 12, "Expected 12 columns")

    def test_not_less_than_12_columns(self):
        self.assertFalse(self.df.shape[1] < 12, "Too few columns")

    def test_not_more_than_12_columns(self):
        self.assertFalse(self.df.shape[1] > 12, "Too many columns")

if __name__ == '__main__':
    unittest.main()