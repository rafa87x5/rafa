print()

numbers = [1, 2, 3, 4, 5]

index = 3


# def function that takes two arguments, first the list and second integer that will be the index
def sum_recursion(x, y):
    # this code here x will hold the  slicing of the list, (y) being the index point to stop and to add to the sum, y+1 to include the index given
    x = x[:y+1:1]
    # add will use sum function to add the sliced list
    add = sum(x)

    return add


print(sum_recursion(numbers, index))


# def function to return the largest number from a given list
def largest_number(x):
    # sorted_list will contain the given list in order from smallest to biggest using sorted function
    sorted_list = sorted(x)
    # big_number v ariable will hold the biggest from the sorted list by slicing the sortefd list given -1 index, which is the last number
    big_number = sorted_list[-1]

    return big_number


# print(largest_number(numbers))

def factorial(n):
    # Base case: 0! = 1
    if (n < 0):
        return 0
    else:
        # Recursive case: n! = n * (n - 1)!
        return n + factorial(n - 1)