# Homework 3, mileage.py
#
# Eric Kye
#
# We are finding the average mileage needed by asking the user to input the numbe
# of miles travled and dividing that by the nunber of gallons needed also inputed by
# the user. We will loop through and continue to ask until the user clicks the return button


print("Your Personal Fuel Economy")
# Holding variable for the total amount of miles added to during each iteration
miles_total=0

# Holding variable for the total amount of gallons added to during each iteration
gallons_total=0


# Infinite loop, we break out the loop when the user clicks the enter or return key
while True:
    miles=input("Number of miles traveled (or enter to exit):")
    # We check for if the input is nothing, if this condition is met we break out of the loop 
    if miles=='':
        break

    # Convert the user input into an int after we can confirm it is not an empty string
    miles=int(miles)
    # Ask the user to input the totala mount of gallons and convert it into an int
    gallons=int(input("Number of gallons needed:"))

    # We add to the total amount of miles during each loop, we add from the total miles and the miles inputted by the user
    miles_total=miles_total+miles

    # We add to the total amount of gallons during each loop, we add from the total gallons and the gallons inputted by the user
    gallons_total=gallons_total+gallons

    # Print the mileage this tank, we divide miles by gallon, we also format it into a string to be precise to one decimal point
    print("Mileage this tank:", ("{:.1f}".format(miles/gallons)))
    
# We create a final average variable that accounts for all iterations, we divide the total number of miles by the total number of gallons
average=miles_total/gallons_total

# We print and format the final average mileage and format it to be precisely one decimal point
print("Average mileage:","{:.1f}".format(average))

    


