import random
randomNumber= random.randint(1,9)
wins= 0
chances= 0

while wins== False:
    guess= input("Enter a number: ")
    chances+=1
    if randomNumber==int(guess):
        print("You won!")
        print("Number of turns you have used: ",chances)
        wins == True
        break
    else:
     if randomNumber>int(guess):
        print("Your Guess was low, Please enter a higher number")
     else:
        print("your guess was high, please enter a lower number")