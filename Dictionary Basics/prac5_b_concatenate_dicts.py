# a Python script to concatenate the following dictionaries to create a new one.
# Using update()

dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict4 = {}
print("Original Dictionaries:")
print(dict1)
print(dict2)
print(dict3)
for d in (dict1, dict2, dict3): 
    dict4.update(d)
print("Concatenated Dictionary: "+str(dict4))
