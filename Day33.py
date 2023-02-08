def inter_section(a, b):
    inter_list = tuple([i for i in a if i in b])
    return inter_list


list1 = [1, 4, 9, 7, 6]
list2 = [2, 2, 4, 6, 9]

print(inter_section(list1, list2))
