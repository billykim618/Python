import random

face = random.randint(1, 13)
suit = random.randint(1, 4)

if 1 == face:
    face = "Ace"
elif 2 == face:
    face = "Two"
elif 3 == face:
    face = "Three"
elif 4 == face:
    face = "Four"
elif 5 == face:
    face = "Five"
elif 6 == face:
    face = "Six"
elif 7 == face:
    face = "Seven"
elif 8 == face:
    face = "Eight"
elif 9 == face:
    face = "Nine"
elif 10 == face:
    face = "Ten"
elif 11 == face:
    face = "Jack"
elif 12 == face:
    face = "Queen"
elif 13 == face:
    face = "King"

if 1 == suit:
    suit = "Spades"
elif 2 == suit:
    suit = "Clubs"
elif 3 == suit:
    suit = "Diamonds"
elif 4 == suit:
    suit = "Hearts"

print("The card you picked is the " + face + " of " + suit)

# CONSOLE OUTPUT:
# The card you picked is the Six of Spades
#
# Process finished with exit code 0

# The card you picked is the Three of Clubs
#
# Process finished with exit code 0

# The card you picked is the Jack of Clubs
#
# Process finished with exit code 0
