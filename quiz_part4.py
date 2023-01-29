# Homework 2  quiz_part4.py
#
# Eric Kye, Juan Melesio
#
# We are asking more multiple choice questions and giving feedback
# to the input user if their responses is correct or not
# We are now also tracking the amount of correct answers given by the user
# We add a new question called the Genius question at the end of the quiz

correct=0
#this is the variable that holds the amount of correct answers to be given at the end


print("ART AND LITERATURE: Who painted Starry Night?")
#this is the main prompt/question we are asking

print("a. Vincent van Gogh")
print("b. Michelangelo")
print("c. Leonardo da Vinci")
#the three print statements above are the answer options we give to the input user

choice=input("Enter your choice:")
#string variable that holds the response given by the user when prompted to answer


if choice=='a':
    print ("Correct!")
    correct=correct+1 #if the answer is correct, we add one to the int variable 
    

else:
    print ("The correct answer was a")
#if and else statement that checks if the response given by the user is the correct
#answer which is 'a'. If it's correct we respond with correct and if it's incorrect we
#provide the correct answer


#**** all of the comments made previously for each statemnt apply to each corresponding
#part/ we are just repeating the question asking process for more questions




print("ENTERTAINMENT: How many oscars did Alfred Hitchcock win?")

print("a. None")
print("b. One")
print("c. Two")

choice=input("Enter your choice:")

if choice=='a':
    print ("Correct!")
    correct=correct+1
else:
    print ("The correct answer was a")




print("GEOGRAPHY: Which is the largest ocean?")

print("a. Pacific")
print("b. Atlantic")
print("c. Indian")

choice=input("Enter your choice:")

if choice=='a':
    print ("Correct!")
    correct=correct+1
else:
    print ("The correct answer was a")



print("HISTORY: Who was the first U.S. president to appear on a coin?")

print("a. Washington")
print("b. Lincoln")
print("c. Jefferson")

choice=input("Enter your choice:")

if choice=='b':
    print ("Correct!")
    correct=correct+1
else:
    print ("The correct answer was b")


print("SCIENCE AND NATURE: Can pigs swim?")

print("a. Yes")
print("b. No")
print("c. Only in salt water")

choice=input("Enter your choice:")

if choice=='a':
    print ("Correct!")
    correct=correct+1
else:
    print ("The correct answer was a")




print("SPORT AND LEISURE: What color is the middle Olympic ring?")

print("a. Red")
print("b. Blue")
print("c. Black")

choice=input("Enter your choice:")

if choice=='c':
    print ("Correct!")
    correct=correct+1
else:
    print ("The correct answer was c")








print("GENIUS: What is D divided by X?")
choice=input("Enter your answer:")



if (choice=='50' or choice=="L"):
    #boolean 'or'  that  looks through the whole parantheses seaching for a true
    #if one is true, they are both true
    print("Correct!")
    correct=correct+1
else:
    print("Correct answers were L or 50")



print("Your final score is", correct)





















