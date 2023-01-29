while True:
   year = input("What year were you born?")
   try:
        year=int(year)
   except:
       continue
   break
print(year, "was a great year")
