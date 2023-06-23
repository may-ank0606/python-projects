import random

def roll_dice():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

def main():
    play_again = True
    while play_again:
        input("Press Enter to roll the dice...")
        dice_value = roll_dice()
        print("The dice rolled and you got:", dice_value)

        play_again_input = input("Do you want to roll again? (y/n): ")
        play_again = play_again_input.lower() == "y"

    print("Thanks for playing!")

if __name__ == '__main__':
    main()
