import unittest
from main import subtract

class TestSubtraction(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)

if __name__ == "__main__":
    unittest.main()
