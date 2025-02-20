import random

def print_dice(number):
    print(" _______ ")
    
    if number == 1:
        print("|       |")
        print("|   *   |")
        print("|_______|")
    elif number == 2:
        print("| *     |")
        print("|       |")
        print("|_____ *|")
    elif number == 3:
        print("| *     |")
        print("|   *   |")
        print("|_____ *|")
    elif number == 4:
        print("| *   * |")
        print("|       |")
        print("|_*___*_|")
    elif number == 5:
        print("| *   * |")
        print("|   *   |")
        print("|_*___*_|")
    elif number == 6:
        print("| *   * |")
        print("| *   * |")
        print("|_*___*_|")

dice_value = random.randint(1, 6)
print_dice(dice_value)
