def count_dots(word):
    m = word.split(".")
    return f'The string has {len(m)-1} dots'


print(count_dots("F.i.s.h.e.s."))

