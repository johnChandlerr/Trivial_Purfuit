import unittest
import definitions
from Trivial_Purfuit.src.player_token.player_token import PlayerToken


class TestPlayerTokenInit(unittest.TestCase):
    def test_empty_token(self):
        test_token = PlayerToken("Jace")
        self.assertEqual(PlayerToken.check_cake_piece(test_token,"people"), False)

class TestPlayerTokenAward(unittest.TestCase):
    def test_empty_token(self):
        test_token = PlayerToken("Steve")
        test_token.award_cake_piece("people")
        self.assertEqual(PlayerToken.check_cake_piece(test_token,"people"), True)


if __name__ == '__main__':
    unittest.main()
