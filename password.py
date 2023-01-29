# Homework 4, password.py
#
# Eric Kye
#
# We are going to ask the user to input a password. We will then see if the user
# has specific things that make a good password. 

# we have boolean values set to false, will use later in if statement
upper=False
lower=False
digit=False
special=False


# ask user to input password
password=input("Enter password:")
# finds the length of the password and prints it out
print ("Length:" , len(password))



# we loop through each letter in the password
for letter in password:

    # for all of these if statments, we check if the condition is met. If it is we set the related boolean value to true. 
    if letter.isupper():
        upper=True
        
    if letter.islower():
        lower=True
        
    if letter.isnumeric():
        digit=True
        
    if letter =='@' or letter=='#' or letter=='$' or letter =='!':
        special=True


if lower==True:
    print("Has lower case")
if upper==True:
    print("Has upper case")
if digit==True:
    print("Has digit")
if special==True:
    print("Has special")

