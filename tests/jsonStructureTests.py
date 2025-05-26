import unittest
import json

class TestJSONStructure(unittest.TestCase):
    def setUp(self):
        with open("data.json", encoding="utf-8") as f:
            self.data = json.load(f)

    def test_each_row_has_12_fields(self):
        for i, row in enumerate(self.data):
            self.assertEqual(len(row), 12, f"Row {i} has {len(row)} fields, expected 12")

if __name__ == '__main__':
    unittest.main()
