#coin_flipper.py


import random


coin= random.choice(["h", "t"])

guess=input("Enter h or t")

if coin==guess:
    print("Correct")
else:
    print("L Bozo ur wrong")


if coin=="h":
    print("Heads")
else:
    print("Tails")
