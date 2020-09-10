from unittest import TestCase
from app.mergesort import merge_sort
from app.Player import Player


class TestMergeSort(TestCase):
    def test_merge_sort(self):
        """Test if the list is sorted correctly using Player objects

        The expected order is: P4, P2, P3, P1. For us to validate this, we test distinct properties on these objects

        Positions 0 and 3 are tested for Player.dod as they are both unique

        Positions 1 and 2 are tested for Player.dob due to their distinct values. Testing Player.dod for these positions
        are unlikely as both objects have "G" as their Player.dod
        """

        players = merge_sort([
            Player("G", "H", "I", "J", "K", "L"),  # P1
            Player("A", "B", "C", "D", "E", "G"),  # P2
            Player("A", "B", "D", "E", "F", "G"),  # P3
            Player("A", "B", "C", "D", "E", "F"),  # P4
        ])

        self.assertEqual(
            [players[0].dod, players[1].dob, players[2].dob, players[3].dod],
            ["F", "E", "F", "L"]
        )