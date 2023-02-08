def nested_lists(*args: list):
    list1 = []
    for i in range(len(args)):
        for j in args:
            list1.append(j)
        break

    return list1


print(nested_lists([1, 2, 4, 5], [3, 9, 7, 3]))
