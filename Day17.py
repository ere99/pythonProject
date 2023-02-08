import random

num = random.randint(0, 10)


def user_name():
    name = input('What is your name?; ')
    name = name[::-1]
    username = name + str(num)
    return f'Your username is {username}'


print(user_name())
