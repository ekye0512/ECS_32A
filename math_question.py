#math_question.py
#ECS32A
#Ask a math question

expression="5*4"

solution = 5*4

ans= input("What is "+expression+"?")
ans=int(ans)

if ans!= solution:
    print ("Incorrect!")
    print("The correct answer is ",solution)

else :
    print ("Correct!")








