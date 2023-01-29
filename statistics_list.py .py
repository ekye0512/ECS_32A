#statistics_list.py


filename=input("Enter filename:")



infile=open(filename)


nums=[]

for line in infile:
    line=line.strip()

    num=float(line)

    nums.append(num)


print("Count", len(nums))

print("Sum", sum(nums))

print("Max", max(nums))



print("Min", min(nums))


print("Average", sum(nums)/len(nums))


