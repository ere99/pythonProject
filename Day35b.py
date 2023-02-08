def find_index(arr: list, n: int) -> list:
    list1 = []

    # using enumerate to find index of integer
    for i, j in enumerate(arr):
        if j == n:
            list1.append(i)
        # if integer not in list
        if n not in arr:
            for j in arr:
                list1.append(n)
            return list1

    return list1


list1 = [1, 2, 4, 6, 7, 7]


print(find_index(list1, 7))
print(find_index(list1, 8))
