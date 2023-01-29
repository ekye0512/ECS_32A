file_name=input("Enter filename:")

infile=open(file_name, "r")

for line in infile:
    line=line.strip()
    print(line)
