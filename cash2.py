# Homework 4, cash2.py
#
# Eric Kye
#
# We modify the cash program to be more inclusive. We want to be able to find the total items and total price for all text files, not just one specific one.
# We have to do the same thing as the cash program but eliminate values that aren't a digit. 

print("Cash register")

# Holding running variable for items and total price that will be added to during each iteration
items=0
total =0


# Prompt user to input name of textfile
filename=input("Enter file of prices:")

# We open the textfile
infile=open(filename)


# We loop through each line in the file
for line in infile:

    # We strip out the white space and the dollar sign becuase it isn't a digit value
    line=line.strip()
    line=line.strip("$")
    

    # We use try and except to prevent a system crash. We try to convert the contents of the file for each line into a floating point
    try:
        num=float(line)
        
    # If it is a value that isn't a digit, we continue back to the start of the loop until a digit is given       
    except:
        continue
            
                     
# Through each iteration we add the number of items by 1
    items=items+1

    # Through each iteration we add the previous price total with the floating value we get from the new line
    total=total+num

# We format the floating point into a string with a dollar sign to show a monetary value
formatted_str= "${:.2f}".format(total)


print ('File contained', items, "items totaling", formatted_str)

    

    
    
