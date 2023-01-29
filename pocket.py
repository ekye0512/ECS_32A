# Homework 3, pocket.py
#
# Eric Kye
#
# We ask the user to input how many quarters, dimes, nickels, pennies they have
# and we have to calculate the amount and make sure to format the floating point
# to 2 decimal points


# Create a constant value for each coin value to refer to it later in code
QUARTER_VALUE=0.25
DIME_VALUE=0.10
NICKEL_VALUE=0.05
PENNY_VALUE=0.01


print ("Pocket change calculator")


# Ask user how many of each coin they have and convert it into an int
quarter=int(input("How many quarters?"))
dime=int(input("How many dimes?"))
nickel=int(input("How many nickels?"))
penny=int(input("How many pennies?"))


# Multiply each coin with their value to get the total value gained from each coin
quarter=quarter*QUARTER_VALUE
dime=dime*DIME_VALUE
nickel=nickel*NICKEL_VALUE
penny=penny*PENNY_VALUE


# Add all of the coin values to get a total of all of the coins combined
amount= quarter+dime+nickel+penny


# Formats the floating point amount from the total coin value we added into two decimal points
formatted_str = "${:.2f}".format(amount)


print("You have", formatted_str)








        





