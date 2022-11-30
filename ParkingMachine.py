class ParkingMachine:
    """An object of this class represents a car parking machine."""

    # class variable
    area_id = 1

    def __init__(self):
        """Call ParkingMachine() to create a Parking Machine."""
        self.total = 0
        self.amount = 0
        self.costPerHour = 10

    def insert_money(self, amount):
        """Insert the specified amount of money."""
        if amount > 0:
            self.amount += amount

    def print_ticket(self):
        """Buy ticket. Text representing the ticket is returned."""
        text = "Parking ticket\n"
        text += "Valid for area: " + str(ParkingMachine.area_id) + "\n"
        text += "Valid for " + str(self.amount * 1.0 / self.costPerHour) + " hours.\n"
        self.total += self.amount
        self.amount = 0
        return text


class Test:
    """A test of Parking machines"""
    def __init__(self):
        """Call Test() to make at Test object."""
        self.machine1 = ParkingMachine()
        self.machine2 = ParkingMachine()

    def run(self):
        """run the test"""
        self.machine1.insert_money(30)
        print(self.machine1.print_ticket())

        self.machine1.insert_money(50)
        print(self.machine1.print_ticket())

        self.machine2.insert_money(40)
        print(self.machine2.print_ticket())

        print("Parking machine 1 total:", self.machine1.total)
        print("Parking machine 2 total:", self.machine2.total)


test = Test()
test.run()
test.run()
