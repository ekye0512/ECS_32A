# Homework 4, cash.py
#
# Eric Kye
#
# We prompt the user to input the name of the text file. The text file has 4 number values representing the prices for certain items.
# We have to open the contents in the file and count the number of items and the total price of all the items combined. 

print("Cash register")

# Running variable that we will add to during each iteration 
items=0
total =0

# Prompt the user to input the name of the file
filename=input("Enter file of prices:")

# We open the file that the user told us to 
infile=open(filename)


# We loop through each line in the file
for line in infile:

    # We get rid of the white space created with each new line
    line=line.strip()

    # We convert each line to a floating point value to represent money
    num=float(line)

    # Through each iteration we add the number of items by 1
    items=items+1

    # Through each iteration we add the previous price total with the floating value we get from the new line
    total=total+num

# We format the floating point into a string with a dollar sign to show a monetary value
formatted_str= "${:.2f}".format(total)


print ('File contained', items, "items totaling", formatted_str)
