import random


def rollDice():
    # Initialize 2 random numbers and add them for a sum.
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    total = num1 + num2

    return total, num1, num2


def gameWithPoint(point):
    # Initialize 2 random numbers and add them for a sum.
    total, num1, num2 = 0, 0, 0

    while total != point and total != 7:
        total, num1, num2 = rollDice()
        print("You rolled", num1, "+", num2, "=", total)

        if total == point:
            print("You win!")
        elif total == 7:
            print("You lose!")


def main():
    # Declare and initialize four different integers.
    total, point, num1, num2 = 0, 0, 0, 0

    total, num1, num2 = rollDice()

    # If you roll 7 or 11, you win.
    print("You rolled", num1, "+", num2, "=", total)
    if total == 11 or total == 7:
        print("You win!")
    # If you roll 2, 3, or 12, you lose.
    elif total == 2 or total == 3 or total == 12:
        print("You lose!")
    # Otherwise, your roll is now your point, then keep rolling until you get your point again or a 7.
    else:
        point = total
        print("Point is", point)
        gameWithPoint(point)


main()  # Invoke main method

