# Python program to sum all the items in a dictionary.

def returnSum(dict):
 
    sum = 0
    for i in dict.values():
        sum = sum + i
 
    return sum
 
 
# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Original Dictionary: "+str(dict))
print("Sum :", returnSum(dict))