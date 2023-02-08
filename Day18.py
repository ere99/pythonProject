def any_num(*args):
    ave = sum(args)/len(args)
    return f'The average is {ave}'


print(any_num(19, 21))
