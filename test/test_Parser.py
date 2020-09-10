from unittest import TestCase
from app.Parser import Parser


class TestParser(TestCase):
    def test_ENOENT(self):
        """Test if class gracefully handles files not found (silently fail to empty lists are okay)
        :return:
        """
        stream = Parser("_chess-players.csv")

        self.assertFalse(stream.list)

    def test_CSV_parse(self):
        """Test if parsing CSV works fine (headers do not count and will fail)
        :return:
        """
        stream = Parser("chess-players.csv")

        self.assertGreater(len(stream.list), 0)