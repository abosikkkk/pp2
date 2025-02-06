#Write a Python function that checks whether a word or phrase is palindrome or not. 
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

def isPalindrome(s):
    s=s.lower()
    return s==s[::-1]

s=input()
if isPalindrome(s):
    print("Palindrome")
else:
    print("Not a Palindrome")