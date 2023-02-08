def index_position(a):
    index = []
    for i, item in enumerate(a):
        if item.islower():
            index.append(i)
    return index


print(index_position('LovE'))
