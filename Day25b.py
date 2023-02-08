str1 = "the love is real"


def read_backwards(n: str) -> str:
    x = []
    for i in n.split()[::-1]:
        x.append(i)
    return ' '.join(x)


print(read_backwards(str1))
