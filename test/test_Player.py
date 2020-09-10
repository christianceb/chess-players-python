from unittest import TestCase
from app.Player import Player


class TestPlayer(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPlayer, self).__init__(*args, **kwargs)

        self.player1 = Player("A", "B", "C", "D", "E", "F")
        self.player2 = Player("G", "H", "I", "J", "K", "L")
        self.player3 = Player("A", "B", "C", "D", "E", "G")
        self.player4 = Player("A", "B", "D", "E", "F", "G")
        self.player5 = Player("Le", "Quick", "Browne", "Focks", "Jumps", "Over");

    def test_eq(self):
        """Test equality override on Player class on 1 object"""
        self.assertEqual(self.player1, self.player1)

    def test_ne(self):
        """Test inverse of equality override on Player class"""
        self.assertNotEqual(self.player2, self.player1)

    def test_lt(self):
        """Test "less than" override on Player class"""
        self.assertLess(self.player1, self.player3)

    def test_lt2(self):
        """Test "less than" override on Player class where the higher value is determined in the middle of the
        properties being evaluated
        """
        self.assertLess(self.player1, self.player4)

    def test_gt(self):
        """Test "greater than" override on Player class"""
        self.assertGreater(self.player2, self.player1)

    def test_contains(self):
        """Test if player contains certain keywords and is case insensitive"""
        self.assertTrue(self.player5.contains("V"))