# Homework 3, roth.py
#
# Eric Kye
#
# We will ask the user to input initial deposit amount and annual percent rate
# We will then loop through until the initial deposit is doubled and keep track
# of the months it takes to double this initial deposit amount

# Asks user to input initial deposit amount and converts it into a float
deposit=float(input("Enter an initial Roth IRA deposit amount:"))

# Asks user to input annual percent rate and converts it into an int
APR=int(input("Enter an annual percent rate of return:"))

# Holding varaible that keeps track of the months and will get added to during each interation
month=0

# Variable to keep track of the current value in the account after the interest amount is added
current_value=deposit 


# We loop until the condtion that our initial deposit is doubled
while current_value< (2*deposit):
    
    # How we get the monthly value needed to add to our current value, it divides the fraction of the apr by 12 because their are 12 months
    added_interest = current_value * (APR / 100) / 12

    # We add to the current value with the amount calculated from the equation above through each loop
    current_value=current_value+added_interest

    # Add a month to every interation which simulates a month being passed
    month=month+1

    # Formats the current value to 2 decimal points and a $ sign to present it as a money value
    formatted_str= "${:.2f}".format(current_value)

    # Convert month to string to concatenate during print so there is no space between the month and ":"
    month_str=str(month)

    print("Value after month", month_str+":", formatted_str)


    


# Convert apr amount to string to easily add the percent sign we need to present it
APR_STR=str(APR)

print("It will take", month,"months to double your investment with a "+APR_STR+"% return.")

    


