# Homework 3, ticket.py
#
# Eric Kye
#
# This program computes ticket prices based on ages and if they went to college
# We ask the user to input their age first and then we assign values from there
#

# Ask for age and convert the string into an int
age=int(input("Enter age:"))


# If age is younger than 3, price is free,
# We check the next conditions based on age, we use boolean 'and' becuase we want to
# make sure the condtions we set in the if statements are 100% accurate
if age<3:
    print("Price: FREE")
elif age>=3 and age<=12:
    print("Price: $29.95")
elif age >=13 and age <=17:
    print("Price: $39.95")
elif age>=65:
    print("Price: $39.95")

# Above we checked for every age category except adults, 
# in the else statement we indent and have another if statement which asks if they are in college
else:
    college=input("College ID? (y/n)")
    if college=='y':
        print("Price: $39.95")
    else:
        print("Price: $49.95")


        
