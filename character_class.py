from player import Player


class Character(Player):
    class_types = ["warrior", "mage", "archer"]
    char_class = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._char_class = kwargs['char_class'] if 'char_class' in kwargs['char_class'] else "dName"

    def warrior(self):
        ...

    def archer(self):
        ...

    def mage(self):
        ...
