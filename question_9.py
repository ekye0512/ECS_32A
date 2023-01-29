inword = input("Enter word:")
pirate = " Aaargh!"    # what the pirate will say
for c in inword:
    pirate = c.upper()+pirate
print(pirate)
