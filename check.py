# Homework 4,  check.py
#
# Eric Kye
#
#


number=input("Enter your 8-digit card number:")
valid = len(number)==8

nums=[]
index_space=0
int_list=[]
index1=-1
index2=-2
first_list=[]
second_list=[]
str_list=[]
split_list=[]

index_of_split=0




for i in range (0,len(number)):
    
    nums.append(number[i])

    if number[i]==' ':
        index_space=i
        nums.pop(index_space)

for numbers in nums:
    int_list.append(int(numbers))


while index1> (len(number)*-1):
    first_list.append(int_list[index1])
    index1=index1-2


sum1=sum(first_list)






while index2> (len(number)*-1):
    second_list.append((int_list[index2])*2)
    index2=index2-2


for i in second_list:

    str_list.append(str(i))


index_of_split=len(str_list)-1
index_of_index=len(str_list[index_of_split]


for i in range (index_of_split):


    split_list.append(str_list[i][0])
    

    
    









    


    
    

    
    
    

  
    
                       



    

    

   

    
    






