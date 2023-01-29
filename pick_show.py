import random

humans=0
orphan_black =0
westworld=0

for i in range(1000000):

    show= random.randint(1,3)
    
    if show==1:
        humans=humans+1
    elif show==2:
        orphan_black=orphan_black+1
    else:
        westworld=westworld+1

if humans>orphan_black and humans>westworld:
    print("Humans")
elif westworld>orphan_black and westorld>humans:
    print("Westworld")
elif orphan_black>humans and orphan_black>westworld:
    print("Orphan Black")


print("H", humans)
print("O", orphan_black)
print("W", westworld)
    



