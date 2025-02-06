#Write a program which can filter prime numbers in a list by using filter function. 
#Note: Use lambda to define anonymous functions.

def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = list(map(int, input().split()))
prime_numbers = list(filter(lambda x: prime(x), numbers))

print("Prime numbers:", prime_numbers)