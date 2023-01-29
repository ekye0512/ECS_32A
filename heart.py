age_input=input("Enter your age:")
age_input=int(age_input)

max_heart=220-age_input

target1= max_heart*.50
target2=max_heart*.85

print ("Your maximum heart rate is", max_heart, "bpm")
print("Your target heart rate is", target1, "-", target2, "bpm")

