register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}


def register_check(reg: dict):
    # Create a count variable
    count = 0
    for value in reg.values():
        if value == 'yes':
            count += 1
    return 'Number of student in school is', count


print(register_check(register))
