#guessing_game.py

import random

guesses=0

pick=random.randint(1,100)


while True:

    print("Thinking of a number 1-100")

    guess= input("Enter Guess")

    guess=int(guess)

    if guess<1 or guess>100:
        continue


    guesses=guesses+1




    if guess==pick:
        print("Correct")
        break

    elif guess<pick:
        print("Too low")
    else:
        print("Too high")


print(guesses)
