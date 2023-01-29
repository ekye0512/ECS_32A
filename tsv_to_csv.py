# tsv_to_csv.py
# 
# Convert a tsv file to csv
filename = input("Enter filename:")
infile = open(filename)
filename = input("Enter output filename:")
outfile = open(filename, "w")

# Loop over each line of the file splitting it
# into values (a.k.a. columns) on "\t" and
# re-joining them using "," 
for line in infile:
    line = line.rstrip("\n")
    if "," in line:
        print("Cannot convert file with comma.")
        break
    line = line.replace("\t",",")
    outfile.write(line + "\n")

infile.close()
outfile.close()
