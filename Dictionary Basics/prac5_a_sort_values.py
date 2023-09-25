# a Python script to sort (ascending and descending) a dictionary by value. 
# using sort() and get().
 
# Initialize a dictionary
my_dict = {'red': '# FF0000', 'green': '# 008000',
           'black': '# 000000', 'white': '# FFFFFF'}
print("Original Dictionary: "+str(my_dict))
 
# Sort and print dictionary
print("Sorted dictionary (Ascending):")
for w in sorted(my_dict, key = my_dict.get):
    print(w, my_dict[w])

print("Sorted dictionary (Descending):")
for w in sorted(my_dict, key = my_dict.get, reverse=True):
    print(w, my_dict[w])
