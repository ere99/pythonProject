def largest_number(arr: list):
    # create empty list
    list1 = []
    # remove brackets and spaces in the lists
    n = str(arr).strip('[,]').replace(',', '').replace(' ', '')
    # append the numbers to the empty list
    for i in n:
        list1.append(int(i))
        # sorting the list in descending order
    list1.sort(reverse=True)
    # removing parenthesis and spaces from the sorted
    large_number = int(str(list1).strip('[]').replace(',', '').replace(' ', ''))
    # return a large formatted number
    return 'The largest number is, {:,}'.format(large_number)


n = [3, 78, 9, 0, 2]

print(largest_number(n))
