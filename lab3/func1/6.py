def reverse(s):
    return " ".join(s.split()[::-1])

s = input("Enter a sentence: ")
print(reverse(s))