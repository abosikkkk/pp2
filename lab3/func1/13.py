#Write a program able to play the "Guess the number" - game, where the number 
#to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
"""
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""
import random
print("Hello! What is your name?")
name=input()
print("Well, " + name +  ", I am thinking of a number between 1 and 20.")
print("Take a guess")
r=random.randint(1, 20)
count=0
while True:
    n=int(input())
    if n<r:
        print("Your guess is too low.")
        print("Take a guess")
        count+=1
    elif n>r:
        print("Your guess is too high.")
        print("Take a guess")
        count+=1
    elif n==r:
        count+=1
        break
print("Good job, " + name + "! You guessed my number in " + str(count) + " guesses!")


        