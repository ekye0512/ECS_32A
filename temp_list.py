# Homework 5, temp_list.py
#
# Eric Kye
#
# Create and empty list and store all of the temperatue values into the list
# using the append function


# running holding variable for max and min values and their respective years
min_temp=None
max_temp=None
min_year=''
max_year=''
temps=[]

# Prompt user input for a file name
filename=input("Temperature anomaly filename:")

# Open the file prompted by the user
infile=open(filename)

# ignore and skip past the first line
infile.readline()

# loop through each line in the file
for line in infile:

    # remove the white space created by the '\n' character that comes from each line
    line=line.strip()


    # split the year and temp into two seperate string variables
    (year,temp)=line.split(",")

    # convert the temp to a floating point value
    temp=float(temp)
    # Add each value from each line into the empty list we created
    temps.append(temp)

    # We check the the temp with the holding min and max variable,
    # If the temp is lower than the holding min, we replace the holding min with the temp and assign the year to the holding min year variable
    # We do the same thing for the maxn
    if min_temp==None or temp<min_temp:
        min_temp=temp
        min_year=year
    if max_temp==None or temp>max_temp:
        max_temp=temp
        max_year=year


#print("Min temp:",min_temp,"in", min_year)
#print("Max temp:",max_temp,"in", max_year)
    
print(temps)


    # print out each line looping through
    # print(year,temp)
