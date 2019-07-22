#imports the ability to get a random number
from random import *
#Generates a random integer
aRandomNumber = randint(1, 20)
#For testing: print(aRandomNumber)
tries = 3 #number of tries initially

setnumber = randit(1, 20)
while tries > 0
if guess == setnumber :
print("Congratulations! The Random number is " setnumber ") break
if guess < setnumber :
print (Your guess is lower. Try again)
if guess > setnumber :
print (Your guess is higher. Try again!)

guess = input("Guess a number between 1 and 20(inclusive):")
if not guess.isnumeric():     print("That's not a positive whole number, try again!")
else:
     guess = int(guess) #converts a string to an integer

print(f"Number of tries={tries})
print("you lose")
