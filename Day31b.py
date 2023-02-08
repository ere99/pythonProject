def create_user():
    d = {}  # create an empty dictionary
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    password = input("Enter your password: ")
    # updating the dictionary using update method
    d.update({'name': name})
    d.update({'age': age})
    d.update({'password': password})
    print("User saved. Please login")
    # using while loop to ensure the code runs
    # until user enters correct login details
    while True:
        user_name = input("Please enter your username to login: ")
        password = input("Please enter your password: ")
        if user_name == d.get('name') and password == d.get('password'):
            return "Logged in successfully"
        else:
            print('Wrong password or username please try again')


print(create_user())
