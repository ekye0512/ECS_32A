# Homework 5, moving_ave_csv.py
#
# Eric Kye
#
# Create an outfile csv file and write in it 


min_temp=None
max_temp=None
min_year=''
max_year=''
temps=[]

# Prompt user input for a file name and window size
filename=input("Temperature anomaly filename:")

# Make a csv output file named MovingAve.csv
outfile=open("MovingAve.csv", 'w')

# Write the header to the file
outfile.write("Year,Value\n")



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

# loop slides the window from index k to len(temps) - 1 - k
# for each index we calculate the corresponding year and 
# the average of the elements from temps[index-k] to temps[index+k] inclusive
for index in range(k,len(temps)-k):
    # calculate year from index
    year=index+1880
    # calculate average for the window centered at index
    ave=sum(temps[index-k:index+k+1])/(2*k+1)
    ave_str="{:.4f}".format(ave)
    # print year,average
    #print(year,ave_str,sep=",")

    # convert year to string to we can write in outfile
    year=str(year)
    
    # concatenate strings to write to outfile
    outfile.write(year+','+ave_str+"\n")


# print(year, ave_str, sep=",")





# close the outfile
outfile.close()
