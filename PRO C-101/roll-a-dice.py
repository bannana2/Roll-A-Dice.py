import random

response = 'y'

while response == 'y':
    # Roll the dice (generate a random number between 1 and 6)
    dice_value = random.randint(1, 6)

    # Print the graphical representation of the dice face
    if dice_value == 1:
        print("---------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("---------")
    elif dice_value == 2:
        print("---------")
        print("| O     |")
        print("|       |")
        print("|     O |")
        print("---------")
    elif dice_value == 3:
        print("---------")
        print("| O     |")
        print("|   O   |")
        print("|     O |")
        print("---------")
    elif dice_value == 4:
        print("---------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("---------")
    elif dice_value == 5:
        print("---------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("---------")
    elif dice_value == 6:
        print("---------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print("---------")

    # Ask user if they want to roll again
    response = input("Roll again? (y/n): ").strip().lower()

    # Validate user input
    while response != 'y' and response != 'n':
        print("Invalid input! Please enter 'y' or 'n'.")
        response = input("Roll again? (y/n): ").strip().lower()

print("Goodbye! Thanks for playing.")