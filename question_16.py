def big_sum(n):
    nums=[]
    i=1

    for i in range (n+1):
        nums.append(i)

    return_value=sum(nums)
    return return_value
    
    

result = big_sum(100000000)
print(result)
