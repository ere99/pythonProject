from collections import Counter

names = ["Joseph", "Nathan", "Sasha", "Kelly",
         "Muhammad", "Jabu", "Sarah", "Patel", "Sarah"]


count = []  # Creating an empty list
for name in names:
    if name.startswith("S"):
        # Appending names that start with S to the list
        count.append(name)
        # Using the counter method to return a dictionary
    names = Counter(count)

print(names)
