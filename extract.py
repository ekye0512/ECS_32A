# Homework 4, extract.py
#
# Eric Kye
#
# We prompt the user to enter a phone number. It is our job
# to loop through and put all the digits of the input into a string and
# print out just the digits

# Prompts user to input a phone number
number=input("Enter phone number:")

# String variable that we will add to later
phoneNum=''

# We loop through each string in the input given by the user
for numbers in number:

    # In each string index, we check to see if it is a numeric value
    if numbers.isnumeric():

        # if the index is a numeric value, we will add the index and concatenate the index with the string that holds all the digits 
        phoneNum=phoneNum+numbers


print(" Numbers:", phoneNum)
