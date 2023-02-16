from character_classes import warrior


def main():
    class_types = ["warrior", "mage", "archer"]

    name = input("Enter name: ")
    for i, _ in enumerate(class_types):
        print(i+1, "-", _)
    char_class = input("Choose a character class: ")
    if char_class.strip() == 1:
        player = warrior(name)

    # char_class = input("Type Warrior, Mage, or Archer: ").strip()
    # player = Player(name, char_class)
    #
    # print(f"Welcome, {player.get_name}! You will begin your adventure\n"
    #       f"as a(n) {player.get_char}")


if __name__ == '__main__':
    main()
