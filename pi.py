# Homework 3, pi.py
#
# Eric Kye
#
#



# Import the math module from phyton
import math

# Import the pi constant given by the math module
PI= math.pi

# Holding varaible for the estimate that we will add or subtract to in the loop
estimate=0

# Holding varaible for the denominator that we will add or subtract to in the loop
denominator=1

# numerator value holding variable
num=4

# Ask for a number of terms and convert it into an int
terms=int(input("Number of terms:"))


# We will keep looping until the terms is -
while terms>0:

    # We add to the estimate through each loop, we do estimate + the numerator/ denominator
    estimate=estimate+(num/denominator)
    
    # We multiply by -1 each time to switch the sign of the numerator becuase that is what an infinite series is
    num=num*-1

  
    # Subtract 1 term each loop as it simulates one math operation done for the estimate
    terms=terms-1
    
    # We add by 2 to the denominator each loop becuase that's the rule of this infinite series
    denominator=(denominator+2)


 

# Print the estimate and format it to be 10 decimal points 
print("Estimate of pi:", "{:.10f}".format(estimate))

# Print the error which is from the pi constant - the total estimate, we also format this to 10 decimal points
print("Error:", "{:.10f}".format(PI-estimate))


            
    
