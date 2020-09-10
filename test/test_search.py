from unittest import TestCase
from app.Player import Player
from app.Parser import Parser
from app.mergesort import merge_sort
from app.search import player_bs_l


class TestSearch(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSearch, self).__init__(*args, **kwargs)

        csv = Parser("chess-players.csv")
        players = []

        # Create Player objects from CSV
        for player in csv.list:
            players.append(Player(player[0], player[1], player[2], player[3], player[4], player[5]))

        # Sort Player objects
        self.players = merge_sort(players)

    def test_player_bs_l(self):
        """
        Find Kolev in the list. Doesn't matter how, just find him
        :return:
        """

        self.assertEqual(player_bs_l(self.players, "Kolev", 0, True).last, "Kolev")