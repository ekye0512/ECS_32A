# Homework 3, cash_register.py
#
# Eric Kye
#
# Use an indefinite while loop and each time we loop through we ask for the price
# of an item, each loop we have a holding counting variable that we add to in order
# to keep track of our total

print("Cash register")

# Holding variable for total price that we will add to during each iteration 
total_price=0

# Holding variable for total items inputted that we will add to during each iteration 
items=0

# Format the string into two decimal points with a money sign to make it a monetary value
formatted_str="${:.2f}".format(total_price)

# Infinite loop that will run until our condtion of '' is met
while True:
    price=input("Enter the price of an item:")

    # This is how we break out of the infinite loop, if the enter key is hit, we break out the loop and go straight to printing the final statement 
    if price =='':
        break

    # Convert the input string to a float 
    price=float(price)

    # Add to this each iteration of the value of the item to get the total value
    total_price=total_price+price

    # Add to this each iteration to get the total amount of items the user inputted
    items=items+1
    formatted_str= "${:.2f}".format(total_price)



  

print("You entered",items,"items totaling", formatted_str)
    

     
