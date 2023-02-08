def password_checker():
    errors = []
    while True:
        password = input('Enter your password: ')
        if not any(i.isupper() and i.islower() and i.isdigit() for i in password):
            errors.append("Please add at least one capital letter and digit to your password")
        elif not any(i.islower() for i in password):
            errors.append("Please add at least one small letter to your password")
        elif not any(i.isdigit() for i in password):
            errors.append("Please add at least one number to your password")
        elif len(password) < 8:
            errors.append("Your password is less than 8 characters")
        if len(errors) > 0:
            print('Check the following errors: ')
            print(str(errors))
            del errors[0:]
        else:
            return f'Your password is {password}'


print(password_checker())
