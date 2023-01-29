# Homework 3, tip.py
#
# Eric Kye
#
# To calculate the tip when given a total amount by the user from 15-25%
# We will use a while loop to prevent having to code ten print statements
#

# We ask the user to input the value of the bill total and then we convert it
# into a floating point 
bill= float(input("Enter total bill:"))

# We create a holding variable for our percentage that will be changed in the loop, we start the value at 15
percent=15
# We create a holding variable for our tip total amount which will be changed in the loop
tip_total=0


# Loop through until the condition that our percentage is less than or equal to 25% is met
while percent<=25:
    
    # Multiply the bill input with the percent and then divide by 100 to account for the decimal places that is assumed in a percentage 
    tip_total= (bill*percent)/100

    # Format the percent variable to look nice and say "15%" with no decimal places after that 
    formatted_str = "{:.0f}%".format(percent)
    # Format the tip total variable to only 2 decimal points to ensure it is a possible money value 
    formatted_str2 = "${:.2f}".format(tip_total)


    print (formatted_str, "is", formatted_str2)

    # Add a percentage at the end of the loop each time to go up and to ensure we dont get an infinite loop
    percent=percent+1

    

    
