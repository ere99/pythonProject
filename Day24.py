def average_calories():
    scores = []
    while True:
        score = input('Enter a score or done when quit: ')
        if score == 'done':
            break
        scores.append(int(score))
    return f"Mean of score is {sum(scores) / len(scores):.2f}"


print(average_calories())

