# Homework 5, read_temp_file.py
#
# Eric Kye
#
# We are taking a comma seperated file and our goal is to print out the year and
# temperature and getting rid of the comma. We also want to go past the first
# line which only serves as a header.


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
    # print out each line looping through
    print(year,temp)


