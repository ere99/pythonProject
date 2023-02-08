def vowels_count(a):
    vowels = []
    for word in a.split():
        for i in word:
            if i in 'aeiou':
                if word not in vowels:
                    vowels.append(word)
    return vowels


print(vowels_count('You are so beautiful to have rhythm'))
