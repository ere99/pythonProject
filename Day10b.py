def convert_numbers(n):
    new_list = []
    for num in n:
        new_list.append("{:,}".format(num))
    return new_list


print(convert_numbers([1000000000000, 348593002, 593053333, 334442]))
