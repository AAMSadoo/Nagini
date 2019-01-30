# This is a guess the number game.
import random

print("Hello!What's your name?")
name =input()

while True:
    print("Hello  " + name + " Please enter the password? Hint: It's the color of your soul")
    password = input()
    if password != "black":
        continue
    if password == "black":
        break
    
print ("Access granted to play the guess name")
    


print("well, " + name + " I'm thinking of a number between 1 and 20. Take a guess.")
secretNumber = random.randint(1,20)



for guessesTaken in range(1,7):
    print ("Take a guess")
    guess = int(input())


    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break #This condition is for the correct guess!

if guess == secretNumber:
    print("Good job, " +  name + "! you guessed my number in " + str(guessesTaken) + " guesses.")
else :
    print("Nope the number I was thinking of was " + str(secretNumber))



