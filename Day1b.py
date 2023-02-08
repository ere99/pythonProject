def longest_value(d: dict):
    # Using max and key len to get the longest value

    longest = max(d.values(), key=len)
    return longest


fruits = {'fruit': 'apple', 'color': 'green'}

print(longest_value(fruits))
