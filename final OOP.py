class Shoes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f'Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}'


shoes_list = []


def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                country, code, product, cost, quantity = line.split(',')
                shoes = Shoes(country, code, product, float(cost), int(quantity))
                shoes_list.append(shoes)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def capture_shoes():
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    shoes = Shoes(country, code, product, cost, quantity)
    shoes_list.append(shoes)


def view_all():
    for shoes in shoes_list:
        print(shoes)


def re_stock():
    min_quantity_shoes = min(shoes_list, key=lambda x: x.get_quantity())
    print(f"The shoe with the lowest quantity is: {min_quantity_shoes}")
    response = input("Would you like to add more quantity to these shoes? (yes/no): ")
    if response.lower() == 'yes':
        additional_quantity = int(input("Enter the additional quantity: "))
        min_quantity_shoes.quantity += additional_quantity


def search_shoe(code):
    for shoes in shoes_list:
        if shoes.code == code:
            return shoes
    return None


def value_per_item():
    for shoes in shoes_list:
        value = shoes.get_cost() * shoes.get_quantity()
        print(f'Value for {shoes.product} is: {value}')


def highest_qty():
    max_quantity_shoes = max(shoes_list, key=lambda x: x.get_quantity())
    print(f"The shoe with the highest quantity is: {max_quantity_shoes}")


def menu():
    while True:
        print("\n1. Capture Shoes")
        print("2. View All")
        print("3. Re-Stock")
        print("4. Search Shoe")
        print("5. Value Per Item")
        print("6. Highest Quantity")
        print("7. Exit")

        option = int(input("Enter your option: "))

        if option == 1:
            capture_shoes()
        elif option == 2:
            view_all()
        elif option == 3:
            re_stock()
        elif option == 4:
            code = input("Enter shoe code to search: ")
            result = search_shoe(code)
            if result:
                print(result)
            else:
                print("No shoe found with the given code.")
        elif option == 5:
            value_per_item()
        elif option == 6:
            highest_qty()
        elif option == 7:
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please enter again.")


# Reading data from inventory.txt
read_shoes_data()

# Displaying the menu for user interaction
menu()