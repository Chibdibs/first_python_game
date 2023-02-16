from player import Player


def main():
    name = input("Enter name: ")
    print("Choose a character class")
    char_class = input("Type Warrior, Mage, or Archer: ").strip()
    player = Player(name, char_class)

    print(f"Welcome, {player.get_name}! You will begin your adventure\n"
          f"as a(n) {player.get_char}")


if __name__ == '__main__':
    main()
