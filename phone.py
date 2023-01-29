# Homework 4, phone.py
#
# Eric Kye
#
# We will ask the user to input a number in a specific format.
# It is our job to ensure that the user is inputting the correct format
# by looping through the phone number and checking specific indexes to make sure
# they have the "-".


# We ask a user to input a phone number in the specific format. 
phone = input("Enter number as  ###-###-####:")        


# we have a boolean 'valid' that makes sure the length of the input is 12
valid = len(phone) == 12

# This is the int variable that will represent the index of the string
pos = 0


# We loop through while the length of the input is 12 until the length reaches 12
while valid and pos < 12:

    # We have our first instance of a dash, we go to the index of 3 and make sure there is a dash
    if pos == 3:
        valid = phone[pos] == "-"
    elif pos == 7:
        valid = phone[pos] == "-"
    # we are ensuring that the user inputted a digit 
    else:
        valid = phone[pos].isdigit()
    pos = pos + 1

if valid:
    print("Valid")
# if it reaches this point, the user failed to input the correct format
else:
    print("Invalid")
