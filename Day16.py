def sum_list(lst1: list):
    counta = 0
    for items in lst1:
        for i in items:
            counta += i
    return 'The sum is ', counta


print(sum_list([1, 4, 5, 9, 2], [3, 2, 1]))
