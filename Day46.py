import pandas as pd

table = {
    'year': [2009, 2002, 2009, 2010, 2009],
    'title': ['Brothers', 'Spiderman', 'Watchmen', 'Inception', 'Avatar'],
    'genre': ['Drama', 'Sci-Fi', 'Drama', 'Sci-Fi', 'Fantasy']
}
movies = pd.DataFrame(table)

print(movies)
