#Write a function that takes in a list of integers and returns True if it contains 007 in order
"""
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
"""
def spy_game(nums):
    zero1 = zero2 = seven = False
    for num in nums:
        if num == 0:
            if zero1:
                zero2 = True
            else:
                zero1 = True 
        elif zero1 and zero2 and num == 7:
            return True 

    return False 
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7])) 
print(spy_game([1, 7, 2, 0, 4, 5, 0])) 