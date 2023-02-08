def user_name():
    your_email = input("Enter your email: ")
    user_name = your_email.split('@')[0]
    return f'Your user name is {user_name}'


print(user_name())
