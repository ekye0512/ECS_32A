# Homework 2 quiz_part1.py
#
# Eric Kye, Juan Melesio
#
#We are asking a multiple choice question and giving feedback
# to the input user if their response is correct or not


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

else:
    print ("The correct answer was a")
#if and else statement that checks if the response given by the user is the correct
#answer which is 'a'. If it's correct we respond with correct and if it's incorrect we
#provide the correct answer
