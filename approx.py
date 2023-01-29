# Homework 2 approx.py
#
# Eric Kye
#
# We are asking the user to input two floating point numbers
# This program then compares the numbers and check to see that it's either
# identical, nearly identical, or different


num1=float(input("Enter a number:"))#ask the user for a number and covert it into a floating point

num2=float(input("Enter a number:"))#ask the user for the next number and convert it into a floating point


diff=num1-num2 #find the difference in both numbers to check the extent of its differnce
# to the decimal place



if diff<0:
    diff= diff* (-1)
#find the asbsoulte value of the differnce so we can compare positive numbers


if(diff==0):
    print("Those numbers are identical ")
elif (diff>=0.001 and diff<0.01):
    print("Those numbers are the same to 2 decimal places")
# We use boolean and to check the conditions to ensure that BOTH are true.
# We want our number to be larger than the amount of decimal places but smaller than
# the next value
elif(diff>=0.0001 and diff<0.001):
    print("Those numbers are the same to 3 decimal places")
elif(diff>=0.00001 and diff<0.0001):
    print("Those numbers are the same to 4 decimal places")

elif(diff>=0.000001 and diff<0.00001):
    print("Those numbers are the same to 5 decimal places")

elif(diff>=0.0000001 and diff<0.000001):
    print("Those numbers are the same to 6 decimal places")

elif(diff>=0.00000001 and diff<0.0000001):
    print("Those numbers are the same to 7 decimal places")

elif(diff>=0.000000001 and diff<0.00000001):
    print("Those numbers are the same to 8 decimal places")

elif(diff>=0.0000000001 and diff<0.000000001):
    print("Those numbers are the same to 9 decimal places")

elif(diff>=0.00000000001 and diff<0.0000000001):
    print("Those numbers are nearly identical ")
else:
    print("Those numbers are different")










