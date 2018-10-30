import unittest

class testPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("1")

    def testInits(self):
        self.assertEqual(self.player.points, 0)
        self.assertEqual(self.player.name, "1")


class Player:
    def __init__(self, name):
        self.points = 0
        self.name = name

    def __str__(self):
        return self.name
