import random
user_win=0
computer_win=0
options=["rock","paper","sessior"]
while True:
    userinput=input("Choose type of rock , paper , sessior or Q to quit: ").lower()
    if userinput == "q":
        break

    if userinput not in options:
        continue

    random_number=random.randint(0,2)
        #rock=0 paper=1 sessior=2
    computer_pick=options[random_number]
    print("Computer pick "+computer_pick)
    if userinput == "rock" and computer_pick == "sessior":
        print("You win")
        user_win+=1
        

    elif userinput == "sessior" and computer_pick == "paper":
        print("You win")
        user_win+=1
        

    elif userinput == "paper" and computer_pick == "rock":
        print("You win")
        user_win+=1
        

    else:
      print("computer is win")
      computer_win+=1
    
print("You win "+str(user_win)+" time!")
print("computer win "+str(computer_win)+" time!")
print("Goodbye!") 
