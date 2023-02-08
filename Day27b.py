
def difference(arr1: list, arr2: list):
    # find items in list 1 not in list 2
    list1 = [i for i in arr1 if i not in arr2]
    # find items in list 2 not in list 1
    list2 = [j for j in arr2 if j not in arr1]
    # concatenate the two lists
    return 'The difference between two sets is ', list1 + list2


print(difference([1, 4, 5, 9], [7, 6, 2, 1]))
