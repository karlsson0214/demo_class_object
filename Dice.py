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


class Test:
    """Class to test Dice."""

    def __init__(self):
        """Call Test() to create a test object."""
        # create a dice object
        self.die = Dice()

    def run(self):
        """Run the test."""
        # Roll the die several times. Show result each time.
        for i in range(20):
            self.die.roll()
            print(self.die.number)


class Test2:
    """Class to test five dice."""
    def __init__(self):
        """Call Test2() to create a test object."""
        # list of dice
        self.dice = []
        # Add 5 dice to list.
        for i in range(5):
            self.dice.append(Dice())

    def run(self):
        """Run the test."""
        # Roll 5 dice. Show result. Re roll.
        for i in range(10):
            print("Roll five dice.")
            for die in self.dice:
                die.roll()
                print(die.number, end=" ")
            print()
            print()


test = Test()
test.run()

test_2 = Test2()
test_2.run()
