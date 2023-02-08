import random

random_number = random.randint(0, 10)

def guess_number():
    c = 0
    while c < 4:
        guess = int(input("Guess a number between 1 and 10: "))
        c += 1
        if c == 3:
            print("You have run out of guesses. You lose")
            break
        elif guess > random_number:
            print('Your guess is too high, Try again')
        else:
            return 'Correct. You win'

    return ''


print(guess_number())
