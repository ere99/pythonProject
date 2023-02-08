from emoji import emojize


def Python_sakes(n: int):
    # the loop to determine the number of ros of the pyramid
    for i in range(0, n):
        # the loop that determines number of columns
        for j in range(n, i, -1):
            # print space between the snake signs
            print(end=" ")
        for k in range(0, i):
            # printing the snake emoji
            print(emojize(':snake:'), end="  ")
        print("\n")


