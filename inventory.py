
print()
# a class called Shoe
class Shoe:
    # constructor with 4 argumentes
    def __init__(self, country, code, product,cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # get cost method
    def get_cost(self):
        return self.cost
    #get quantity method
    def get_quanty(self):
        return self.quantity

    def __str__(self) -> str:
        
        return f"Country is {self.country}, shoe code is {self.code}, shoe model is {self.product}, cost of the shoe is {self.cost}, and the quantity for this model is {self.quantity}"
#empty list to store the objects
shoes_objects = []
#def function to read the data from txt file called inventory.txt
def read_shoes_data():
    with open("inventory.txt", "r") as file:
        try:
            #a for loop to iterate througt the txt file and append object into the list
            # this functions uses try and except for error handling
            for lines in file:
                temp = lines.strip()
                temp = temp.split(",")
                shoes_objects.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))
        except FileNotFoundError:
            print("Error: File not found.")
            return False
        finally:
            
            return True

        
# Def function to create new objects, append the new object to shoes_objects list 
# and then it will be append/written to the txt file 
#this function uses try and except for error handling
def capture_shoes():
   while True:
        create_new_object = input("\nDo you  want to capture a new shoe (yes/no): ").lower()
        if create_new_object == "yes":
                
            while True:

                country_input = input("\nPlease enter the country: ").capitalize()
                #if statement here checks if the input from country_input is a digit input
                #if the input is not digit, and error message will be shown
                if country_input.isdigit():
                    print("Not numbers accepted!")
                    pass
                else:
                    break
            

            code_input = input("\nPlease enter the code: ").upper()
            product_input = input("\nPlease enter the product model: ").capitalize()
            while True:
                #try and except to endure that user only enter numbers
                try:
                    cost_input = float(input("\nPlease enter the cost: "))
                    break
                except ValueError:
                    print("\nJust numbers accepted!")

                finally:
                    pass
            while True:
                #error handling to ensure the user only enter numbers
                try:
                    quantity_input = int(input("\nPlease enter the quatity: "))
                    break
                except ValueError:
                    print("\nJust numbers accepted!")

                finally:
                    pass
            #code here will take all the inputs and append them to the list shoes_objects
            #to save it into the txt file is the user confirm so
            shoes_objects.append(Shoe(country_input,code_input, product_input, cost_input, quantity_input))

            save_shoe__to_file = input("\nAre you sure you want to save the new product? (yes/no) : ").lower()
            if save_shoe__to_file == "yes":

                with open("inventory.txt", "a") as new_object:
                    new_object.write(f"\n{country_input},{code_input},{product_input},{code_input},{quantity_input}")
                    print("\nThe new object has been saved!")

            else:
                break
        elif create_new_object == "no":
            break

        else:
            print("\nWrong choice!!")



# view_all function will display all the objects in the shoes_objects list in a readable maner  
def view_all():
    #if statement to check that the list is no empty,if so appropiate message will be shown
    if not shoes_objects:
        print("There is nothing in the list") 

    else:
        #for loop to iterare over the shoes_objects list and prints each iteration 
        for item in shoes_objects[1:]:
            print(f"\n{item}")
    
    

# re_stock is a function that show the object with the lowest quantity and promp the user
#to re stosck if he wishes to do so
def re_stock():
    #lowest varible here stores the first line for referece and comparation
    lowest = shoes_objects[1]
    #for loop to iterare over the shoes_object list
    for item in shoes_objects[1:]:
        #if statement to check if the quantity of the object is grater than the fisrt itereation 
        # first objects quantity, if so lowest will stores the lowest quantity
        if int(lowest.quantity) > int(item.quantity):
            lowest = item

    
    print(f"The product {lowest.product} has the lowest quantity of {lowest.quantity}")

    while True:
    
            up_date_stock = input("Do you want to add quantity for this shoes (yes/no)? ").lower()
            if up_date_stock != "yes" and up_date_stock != "no":
                print("Wrong choice, try again!")

            elif up_date_stock == "no":
                break

            elif up_date_stock == "yes":
                while True:
                        try:
                    
                            lowest.quantity = int(input("Please enter the new stock quantity: "))
                            break
                            
                        except ValueError:
                            print("Just numbers accepted") 
                        finally:
                            pass
    with open("inventory.txt", "w") as update:
        for item in shoes_objects:
            update.write(str(f"{item.country}, {item.code}, {item.product}, {item.cost}, {item.quantity}\n"))


def search_shoe():
    while True:
        try:
            find_shoe_by_code = input("\nEnter the shoe code: ").upper()
            
            for item in shoes_objects:
                if item.code == find_shoe_by_code:
                    return print(f"\n{item.country}, {item.code}, {item.product}, {item.cost}, {item.quantity}")
                 
            print("Shoe not found!")

        except KeyboardInterrupt:
            print("Search canceled")
            break
       


def value_per_item():
    
    for value in shoes_objects[1:]:
        total_value_per_each_item = int(value.cost) * int(value.quantity)
        print(f"The total stock value for {value.product} is {total_value_per_each_item}")
        
    return 

def highest_quantity():
    highest = shoes_objects[1]
    for item in shoes_objects[1:]:
        if int(highest.quantity) < int(item.quantity):
            highest = item 
        
    return print(f"\nThe product {highest.product} is being for sale, {highest.quantity} units")
    

def main():
    while True:
        try:

            user_choice = int(input('''\nChoose one of the following options:\n
                    1. To get cost of a shoe
                    2. To get the quantity of the shoes
                    3. To capture a shoe and save it to a file
                    4. To view all inventory
                    5. To view the lowest quantity and re-stock
                    6. To search a shoe using the shoe's code
                    7. To view the total value per item
                    8. To view the highest quantity being for sale
                    0. To exit
                    : '''))
            print(type(user_choice))
            if user_choice == 1 :
            
                read_shoes_data()
                print(shoes_objects[1].get_cost())
                
                

            elif user_choice == 2:
                Shoe.get_quanty()

            elif user_choice == 3:
                capture_shoes()

            elif user_choice == 4 :
                read_shoes_data()
                view_all()

            elif user_choice == 5:
            
                read_shoes_data()
                re_stock()
                

            elif user_choice == 6:
                read_shoes_data()
                search_shoe()

            elif user_choice == 7:
                read_shoes_data()
                value_per_item()

            elif user_choice == 8:
                read_shoes_data()
                highest_quantity()

            elif user_choice == 0:
                print("Good bye!!")
                break 
            

            else:
                print("\nInvalid input!")
        
        except ValueError:
            print("\nInput no valid!!")

main()
    
                
            
            




