
list3 = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]


def missing_numbers(arr: list) -> list:
    missing_numz = []
    # find the missing numbers using range
    for i in range(arr[0], arr[-1] + 1):
        if i not in arr:
            missing_numz.append(i)

    return missing_numz


print(missing_numbers(list3))
