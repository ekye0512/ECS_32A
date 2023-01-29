# write_nums.py
#
# Write random floating point numbers to a file
import random

num_lines = int(input("How many numbers? "))
largest = float(input("Largest number? "))
filename = input("Output file name:")

outfile = open(filename, "w") 

for i in range(num_lines):
    # random floating point between 0 and 1
    n = random.random()
    # change the range from 0 to largest
    n = n * largest
    # create output line
    line = str(n) + "\n" 
    # write output line and print to screen
    outfile.write(line)
    print(line, end = "")
    
outfile.close() # close the file
