# Homework 4, cat.py
#
# Eric Kye
#
# We ask the user to input the name of a file. We take the file and open it
# and print each line while also making sure we get rid of the "/n" character.
# We also want to check and make sure the correctly inputs a file name and not
# a random string. 

# We prompt the user to input a file to open
filename=input ("Enter a file name to open:")

# We loop through continually until the loop is broken out  of
while True:

    # We check to see if the input from the user is a valid filename
    try:
        # we open the file in reading 
        infile =open(filename, 'r')

        # loop through each line in the file
        for line in infile:

             # we strip the white space from each line
            line=line.strip()
            print(line)
        # break out of the loop 
        break

    # if the user did not enter a valid file name, we tell them we can't open
    # their file and ask for a filename again
    except:
        print("Could not open", filename)
        filename=input ("Enter a file name to open:")
        




