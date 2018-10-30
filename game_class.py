import unittest
import player_class

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def run(self):
        for user in self.players:
            # do stuff
            return 420
