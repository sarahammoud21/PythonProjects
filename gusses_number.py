import random

top_random=input("Write a top number you want: ")

if top_random.isdigit():
    top_random=int(top_random)
    if top_random<=0:
       print("please enter a number above of 0 next time")
       quit()
else:
    print("please enter a number next time")
    quit()
random_number=random.randint(0,top_random)

guesses=0


while True:
   gusse=int(input("Make a gusse: "))
   guesses+=1
   if gusse==random_number:
      print("You got it!")
      break
   elif gusse>random_number:
    print("The gusses is under of a number")
   elif gusse<random_number:
    print("The gusses is above of a number")
   continue 
print("Number of gusses "+str(guesses)+"")


