def longest_word(a):
    b = []
    for word in a:
        b.append([len(word), word])
    return max(b)


print(longest_word(['Java', 'Pythagoras', 'kos']))
