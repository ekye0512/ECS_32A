# Homework 3, change.py
#
# Eric Kye
#
# We first have to ask the user to input a positive value from 0-100 which will represent
# a value $0.00-$1.00, next we use the mod and floor int divsion feature to divide the value given
# and tell how many of each coin one will have going in descending order from quarter to penny


# Create a constant value for each coin value to refer to it later in code
QUARTER_VALUE=25
DIME_VALUE=10
NICKEL_VALUE=5
PENNY_VALUE=1

# Ask user to enter change and then convert it into a string
value= int(input("Enter change:"))

# First do floor int division just to get the amount of coins for each coin, next
# we use mod to get the remainder which we can continue to use for the next coins
quarter=value//QUARTER_VALUE
value=value%QUARTER_VALUE
print ("Quarters:",quarter)

dime=value//DIME_VALUE
value=value%DIME_VALUE
print ("Dimes:",dime)


nickel=value//NICKEL_VALUE
value=value%NICKEL_VALUE
print ("Nickels:",nickel)


penny=value//PENNY_VALUE
print ("Pennies:",penny)





















        





