import random


class InvalidLevelError(Exception):
    pass


try:
    intro = int(input("Choose level: "))
except ValueError:
    raise InvalidLevelError("The level you selected is not valid!")
if intro <= 0:
    raise InvalidLevelError("The level you selected is not valid!")

computer_number = random.randint(1, 10 * intro)
play = True
while play:
    try:
        player_num = int(input("Gues the number: "))
    except ValueError:
        print(f"Enter a number only!")
        continue
    if player_num == computer_number:
        print("Bravo!!!!")
        play = True if input("Do you want ot play again? [y/n]") == "y" or "Y" else False

    elif player_num < computer_number:
        print("Up")
    else:
        print("Down")
