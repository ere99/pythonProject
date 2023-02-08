def even_or_average():
    avg_num = []
    even_number = []
    while True:
        number = input("Please enter number or done: ")
        avg_num.append(int(number))
        if int(number) % 2 == 0:
            even_number.append(number)
        if len(avg_num) == 5:
            break
    if len(even_number) > 0:
        return f'The largest even number: {max(even_number)}'

    else:
        return f'The average is : {sum(avg_num) / len(avg_num): 2f}'


print(even_or_average())
