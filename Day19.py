def count_words(arr: str):
    words = []
    for word in arr.split():
        words.append(word)
    return f'There are {len(words)} words in the sentence'


print(count_words('Let us run away'))


def count_characters(a):
    a = a.replace(' ', '')
    return f'The string has {len(a)} elements'


print(count_characters('go go anime'))
