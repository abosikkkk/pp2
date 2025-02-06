#Write a function that accepts string from user and print all permutations of that string.

from itertools import permutations

def print_permutations(s):
    for perm in permutations(s):
        print("".join(perm))

s = input("Enter a string: ")
print_permutations(s)
