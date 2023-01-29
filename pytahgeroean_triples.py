# pythagorean_triples.py

# Find all a,b,c less than 100 where a^2 +b^2=c^2
# a<b<c





for a in range (1, 100):
    for b in range(a+1,100):
        for c in range (b+1,100):

            if a**2+b**2==c**2:
                print(a,b,c, sep="-")


