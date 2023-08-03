print()


# def function to do the calculations with 3 arguments
# and return the result of the operation
# and ride an erro if user tries to divide by zero
def calculate(num1, operator, num2):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            return num1 / num2
        else:
            raise ValueError("Invalid operator.")
    except ValueError as ve:
        print(f"Error: {ve}")
    finally:
        print("Calculation finished.")


# def function here opens a file and if file in found the error message will be shown
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    finally:
        print("Finished processing the file.")


# first part of the task to do operatiopns and save the calculations to a txt file
# if user enters other than a integer a error messge will be shown
# while loop to repeat doing operations is user wishes to do so
symbol_operators = ["+", "-", "*", "/"]
while True:
    while True:
        while True:
            try:
                num_1 = int(input("Please enter first number: "))
                break

            except ValueError:
                print("Just numbers accepted")
            finally:
                pass
        while True:
            try:
                operator_1 = input("Please enter the operator (+, -, *, /): ")
                if operator_1 in symbol_operators:
                    break
                else:
                    raise ValueError("Invalid operator")
            except ValueError:

                print("Invalid operator entered!!")
        while True:
            try:
                num_2 = int(input("Please enter second number: "))
                break
            except ValueError:
                print("Just numbers accepted")
        # here the def function is call to do the mathematical operation
        result_1 = calculate(num_1, operator_1, num_2)

        if result_1 is not None:
            print(f"Result: {result_1}")
            # code here will create a txt file and save the equations there
            with open("equation.txt", "a") as equation:
                equation.write(f"\n{num_1} {operator_1} {num_2} = {result_1} ")
        while True:
            more_equations = input("Do you want to continue doing equations (yes/no)? : ").lower()
            if more_equations.isdigit():
                print("no digits accepted")
                continue
            elif more_equations == "no":
                print("no")
                break
            elif more_equations == "yes":
                print("yes")

            else:
                print("please only select yes/no depending on what you want to do")
                continue

        break
    break

# FROM HERE IS THE SECOND PART OF THE TASK
# an empty list to store or the operations made by the user
# an later write the to a txt file
equation_list = []
# while loop to presenting a menu to
# do more calculations
# save calculations to a file
# and read calculations from a saved file
while True:
    try:
        choice = int(input('''\nWould you like to:
                        1. Do more calculation
                        2. Save calculations to a file
                        3. Read your calculations from a file 
                        4. To exit:
                        '''))

        if choice == 1:
            while True:
                try:
                    num1 = int(input("Enter first number: "))
                    break

                except ValueError:
                    print("Just numbers accepted")
                finally:
                    pass
            while True:
                try:
                    operator = input("Enter the operator (+, -, *, /): ")
                    if operator in symbol_operators:
                        break
                    else:
                        raise ValueError("Invalid operator")
                except ValueError:
                    print("Invalid operator entered!!")

            while True:
                try:
                    num2 = int(input("Enter second number: "))
                    break

                except ValueError:
                    print("Just numbers accepted")
                finally:
                    pass

            result = calculate(num1, operator, num2)

            if result is not None:
                print(f"Result: {result}")
                # append function is call here to add each operation to the empty list
                equation_list.append(f"{num1} {operator} {num2} = {result}")

        elif choice == 2:
            # line below ask the user to enter a name for his/her file
            filename = input("Enter the file name to save equations : ")
            # code here will create a txt file,the  open() function receives the variable filename and a add the dot and txt
            # to create the file as a txt file
            with open(f"{filename}.txt", "a") as operations:
                # for loop to iterate the list and write each iteration to the new file
                for equation in equation_list:
                    operations.write(f"\n{equation}")
                print("Equations saved to the file.")

        elif choice == 3:

            # while loop to ask the user to open a file and calling a def function call read_file
            # if file doesnt exist an apropiated error will be shown and ask again for the name of the file
            # while True:
            filename = input("Enter the name of the file you'd like to open or 1 to exit: ").lower()
            if filename == "1":
                exit()

            read_file(f"{filename}.txt")

        elif choice == 4:
            exit()

        else:
            print("Invalid input!")

    except ValueError:
        print("Input no valid!!")
