# Homework 3, car.py
#
# Eric Kye
#
# We have a set value on a car of $42,500, the user has to continually guess
# the value of the car until they get it right, we also have to give hints
# to the user by telling them if their guess is too high or low

# This is a constant value, the price of the car given 
PRICE=42500

print ("Guess the price and win the prize!")

# Holding variable to keep track of how many guesses, will be added to each iteration 
guess_count=0

# We loop through until the condtion that the guess count is greater than 5 is met
while guess_count<=5:
    # We add to the guess count during each loop
    guess_count=guess_count+1

    # We ask the user for a guess and we convert it into an int
    guess=int (input("Enter your guess:"))
    

    # We check if the guesses exceed 5, if it does exceed 5 we print too many guesses and break out of the loop 
    if guess_count>5:
        print("Too many guesses!")
        break
    
    # If the guess is correct, we print that they won the car and break out of the loop 
    if guess == PRICE:
        print("You won the car!")
        break

    # We check compare the prices using boolean statements, if too high we print too high and the same for if the guess is too low
    elif guess>PRICE:
        print("Too high!")
    else:
        print("Too low!")
       


