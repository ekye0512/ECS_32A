#guess_num.py


import random

pick=random.randint(1,3)


print("I'm guessing of a number 1-3")

guess=input("Enter your guess:")
guess=int(guess)

if guess == pick:
    print("Yep")
elif(guess>pick):
    print("Too high")
else:
    print("Too low")
print("I was thinking of", pick)
