#Write a Python function that takes a list and returns a new list 
#with unique elements of the first list. Note: don't use collection set

def unique_list(list_old):
    list_new=[]
    for x in list_old:
        if x not in list_new:
            list_new.append(x)
    return list_new

list_old=[3, 3, 3, 5, 7, 3, 4]
print(unique_list(list_old))