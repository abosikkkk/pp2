#Write a function that computes the volume of a sphere given its radius.

import math
def volume(r):
    V=4/3*math.pi*r**3
    return V

r=float(input())
print(volume(r))