
class Product:

    # product id, 1, 2, 3, 4, ...
    id = 1

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = Product.id
        Product.id = Product.id + 1

    def __str__(self):
        return "id: " + str(self.id) + " " + self.name + " " + str(self.price) + " SEK"


class VendingMachine:

    def __init__(self):
        self.total = 0
        self.amount = 0
        # dictionary with all products
        # key: id of product and value: product
        self.product_dictionary = {}

    def add_product(self, product):
        self.product_dictionary[product.id] = product

    # call when debugging
    # returns a string representation of a vending machine object
    def __str__(self):
        text = ""
        '''
        for product in self.products:
            text += str(product) + "\n"
        '''
        text += "total: " + str(self.total) + "\n"
        text += "amount: " + str(self.amount) + "\n"

        return text

    def get_menu(self):
        text = ""
        for product in self.product_dictionary.values():
            text += str(product) + "\n"
        return text

    def insert_money(self, amount):
        if amount > 0:
            self.amount += amount

    def get_product(self, product_id):
        if product_id in self.product_dictionary.keys():
            # has product
            product = self.product_dictionary[product_id]
            if self.amount >= product.price:
                self.total += self.amount
                self.amount = 0
                return product
        else:
            return None


# Application
def app():
    machine = VendingMachine()

    machine.add_product(Product("Bun", 30))
    machine.add_product(Product("Banana", 10))
    machine.add_product(Product("Apple", 10))

    product_id = 1
    while product_id != 0:
        print("Vending Machine")
        print(machine.get_menu())
        amount = int(input("Insert money: "))
        print(amount, "SEK inserted")
        machine.insert_money(amount)
        # select id = 0 to exit machine
        product_id = int(input("Select product. Use id."))

        product = machine.get_product(product_id)
        if product is None:
            print("Not enough money")
        else:
            print("Pick up your: " + product.name)

        print("Debug info")
        print(machine)
        print("end debug info")
        print()


app()




