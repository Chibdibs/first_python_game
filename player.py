from character_class import Character


class Player:
    hp = 100

    def __init__(self, name, char):
        self._name = name
        self._char = char

    @property
    def get_name(self):
        return self._name

    @property
    def get_char(self):
        return self._char

    # def set_char(self, char):
    #     parsed_char = char.lower()
    #     if parsed_char == "warrior":
    #         self._char = Character(char_class="warrior")
    #     elif parsed_char == "mage":
    #         self._char = Character(char_class="mage")
    #     elif parsed_char == "archer":
    #         self._char = Character(char_class="archer")
    #     else:
    #         print("Invalid character class")

    def attack(self):
        print("Player attacked!")

    def defend(self):
        print("Player defended!")