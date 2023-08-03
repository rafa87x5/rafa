def sum_recursion(lst, index):
    # Base case: if the index is zero, just return the first element
    if index == 0:
        return lst[0]

    # Recursive case: return the sum of the current index and the sum of the elements before it
    return lst[index] + sum_recursion(lst, index - 1)


lista = [1, 2, 3, 4, 5]
print(sum_recursion(lista, 2))