import unittest
from Trivial_Purfuit.src.die.die import Die


class MyTestCase(unittest.TestCase):
    # test roll function, number must between in 1 to 6
    def test_roll(self):
        die = Die()
        for i in range(100):
            die_num = die.roll()
            self.assertTrue(1 <= die_num <= 6)


if __name__ == '__main__':
    unittest.main()
