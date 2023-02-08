def add_reverse(n: list, k: list):
    # creating an empty list
    new_list = []
    if len(n) == len(k):
        for i in range(0, len(n)):
            # adding ad appending corresponding numbers
            new_list.append(n[i] + k[i])
            # reversing new list
            new_list.reverse()
        return new_list
    else:
        return f'Lists have different lengths'


# lists to add and reverse
list1 = [10, 12, 34]
list2 = [12, 56, 78]

print(add_reverse(list1, list2))
