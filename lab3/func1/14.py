import random
def guessnumber():
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

guessnumber()