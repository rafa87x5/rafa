# largest_number.py

def largest_number(numbers):

    # Base Case: if the list has one element, return that element
    if len(numbers) == 1:
        return numbers[0]

    # Recursive Case: compare the first element with the largest number in the rest of the list
    else:
        max_of_rest = largest_number(numbers[1:])
        return max(numbers[0], max_of_rest)


# Test the function
print(largest_number([1, 4, 5, 3]))  # Expected Output: 5
print(largest_number([3, 1, 6, 8, 2, 4, 5]))  # Expected Output: 8