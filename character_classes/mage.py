from character_classes.player import Player


class Mage(Player):
    def __init__(self, name):
        super().__init__(self, name)
        self._name = name
