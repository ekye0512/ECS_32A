cost=input("Enter cost of car:")
cost=int(cost)

driven=input("Enter miles driven per year:")
driven=int(driven)

gas_cost=input("Enter cost of gas:")
gas_cost=int(gas_cost)

eff=input("Efficency in miles per gallon:")
eff=int(eff)

resale=input("Estimated resale value after 5 years:")
resale=int(resale)


gallon=float(driven/eff)
gas_total=gas_cost*gallon
gas_total=gas_total*5

dep=cost-resale



print("Five year cost:",dep+gas_total)

