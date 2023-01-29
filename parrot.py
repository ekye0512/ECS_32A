# Homework 4, parrot.py
#
# Eric Kye
#
# This program we echo what the user inputs and capitalize it. We also stop echoing
# when the user inputs hush. We loop and prompt the user with ">" to input something.
# After we capitalize it and before we print we check if the user inputted hush.


# Indefinite loop, we loop through until a condition is met.
while True:

    # We prompt the user to input something. 
    user_input=input(">")
    

    # We capitalize the inputted string with the string method ".upper()".
    user_input=user_input.upper()

    # Since we capitalize all the inputs, we check if the user inputted "HUSH". 
    if user_input=='HUSH':
        # If they did input any variation of hush regardless of case, we break out of the loop.
        break

    print(user_input)

    

