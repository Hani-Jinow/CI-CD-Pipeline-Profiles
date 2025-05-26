import unittest
import json

class TestJSONRows(unittest.TestCase):
    def setUp(self):
        with open("data.json", encoding="utf-8") as f:
            self.data = json.load(f)

    def test_minimum_900_rows(self):
        self.assertGreaterEqual(len(self.data), 900, "Expected at least 900 rows in data.json")

if __name__ == '__main__':
    unittest.main()
