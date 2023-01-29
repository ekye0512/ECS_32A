

height=int(input("Enter height:"))
width=int(input("Enter width:"))


for row in range (1, height +1):
    for col in range(1,width+1):

        print("{:4.0f}".format(row*col), end="")
    print()
