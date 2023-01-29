# statistics_file.py



filename = input("Enter input filename:")
infile = open(filename)

header=infile.readline()


running_max_cals=None
max_item=None

running_min_carbs=None
min_item=None



for line in infile:


    item,cals,carbs=line.split("\t")

    
    
    cals=int(cals)
    carbs=int(carbs)

    
    if running_min_carbs==None or carbs<running_min_carbs:
        running_min_carbs=carbs
        min_item=item


    if running_max_cals==None or cals>running_max_cals:
        running_max_cals=cals
        max_item=item
 



print("Max Cal", max_item,running_max_cals)

print("Min Carbs", min_item,running_min_carbs)

