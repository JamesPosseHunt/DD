import unittest
from dice import roll_die

class TestRollDie(unittest.TestCase):

    def test_valid_rolls(self):
        for sides in [4, 6, 8, 10, 12, 20, 100]:
            with self.subTest(sides=sides):
                for _ in range(100):  
                    result = roll_die(sides)
                    self.assertGreaterEqual(result, 1)
                    self.assertLessEqual(result, sides)

    def test_one_sided_die(self):
        self.assertEqual(roll_die(1), 1)

    def test_invalid_rolls(self):
        with self.assertRaises(ValueError):
            roll_die(0)
        with self.assertRaises(ValueError):
            roll_die(-3)

if __name__ == '__main__':
    unittest.main()
