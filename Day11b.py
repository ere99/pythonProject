def swap_values(arr: list):
    # Create a variable for first number
    first_number = arr[0]
    # Create a second variable for the last number
    last_number = arr[-1]
    # assign last number to index 1
    arr[0] = last_number
    arr[-1] = first_number
    return arr


print(swap_values([1, 5, 9, 8]))
