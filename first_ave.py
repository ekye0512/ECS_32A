# Homework 5,  first_ave.py
#
# Eric Kye
#
# We have to get the average from a window size we ask the user.
# The range of averages go from the year minus the window and the year plus the window



# running holding variable for max and min values and their respective years
min_temp=None
max_temp=None
min_year=''
max_year=''
temps=[]

# Prompt user input for a file name and window size
filename=input("Temperature anomaly filename:")

k=input("Enter window size:")
k=int(k)

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
    
#print(temps)


    # print out each line looping through
    # print(year,temp)

# Assign an index that is what the user inputted
index = k
# The year we look at is the first year in our file plus the index
year = 1880 + index
# We get the average of the values
ave = sum(temps[index-k:index+k+1]) / (2*k+1)

# Format the string to 4 decimal points
ave_str="{:.4f}".format(ave)


print(year, ave_str, sep=",")
