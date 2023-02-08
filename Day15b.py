names_age = {"Jane": 24, 'kerry': 30, "timmy": 22, "peter": 17}


def your_age():
    # convert name to lowercase
    name = input("Please enter your name: ").lower()
    # use for loop to iterate over the dictionary
    for key in names_age.keys():
        if key == name:
            # use the get method to access a specific value
            return f'Hi, {name}! you are {names_age.get(key)} years old'
    else:
        while name not in names_age.keys():
            age = input("Your name is not in the dictionary, please enter your age: ").lower()
            # update the dictionary with name and age
            names_age.update({name: age})
            return f'Hi, {name}! you are {names_age.get(name)} years old'


print(your_age())
