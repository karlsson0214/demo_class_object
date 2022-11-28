import random


class Dice:
    """An object of this class represent a die with six sides."""
    def __init__(self):
        """Call Dice() to create an object of this class."""
        # number shown on dice
        self.number = 1

    def roll(self):
        """Roll the dice."""
        self.number = random.randint(1, 6)


# create a dice object
die = Dice()

# Roll the die several times. Show result each time.
for i in range(20):
    die.roll()
    print(die.number)


# list of dice
dice = []
# Add 5 dice to list.
for i in range(5):
    dice.append(Dice())

# Roll 5 dice. Show result. Re roll.
for i in range(10):
    print("Roll five dice.")
    for die in dice:
        die.roll()
        print(die.number, end=" ")
    print()
    print()






