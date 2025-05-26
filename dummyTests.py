import unittest

class TestDummy(unittest.TestCase):
    def test_always_passes(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()