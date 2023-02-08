nested_list = [[12, 23, 54, 67], [33, 19, 78]]

new_list = []
# A nested for loop to access the inner list
for arr in nested_list:
    for num in arr:
        # create a list of numbers wanted
        if num in [33, 67, 78]:
            # checking if number already exists before appending
            if num not in new_list:
                new_list.append(num)

print(new_list)
