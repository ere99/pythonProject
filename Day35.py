import string


def check_pangram(sentence):
    list1 = []
    alphabet = string.ascii_lowercase
    # removing white spaces in the string
    sentence = sentence.replace(' ', '')
    for i in sentence:
        if i not in list1:
            list1.append(i)
    list1.sort()
    sentence = ''.join(list1)
    if alphabet == sentence:
        return True
    else:
        return False


print(check_pangram('the quick brown fox jumps over a lazy dog'))
