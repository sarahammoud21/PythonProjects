

print("Welcome to my computer game! ")

letter=input("Do you want to play? ")

if letter.lower() == 'yes':
    print("Let's start the quiz! ")
else: 
    quit()
score=0
answer=input("What dose CPU stand for? ")
if answer.lower() == 'central processing unit':
    print("Correct")
    score+=1
else:
    print("Incorrect ")
answer=input("What dose ML stand for? ")
if answer.lower() == 'machine learning':
    print("Correct")
    score+=1
else:
    print("Incorrect ")
answer=input("What dose RAM stand for? ")
if answer.lower() == 'random access memory':
    print("Correct")
    score+=1
else:
    print("Incorrect ")
answer=input("What dose GPU stand for? ")
if answer.lower() == 'graphic processing unit':
    print("Correct")
    score+=1
else:
    print("Incorrect ")
print("You got "+str(score)+" answer correct! ")
print("You got "+str(score/4*100)+"%")