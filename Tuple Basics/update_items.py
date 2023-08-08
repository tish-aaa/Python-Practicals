#Python program to update an item in a Tuple.
#By converting Tuple to List and changing values using index.

t=("a","b","c")
print("Original Tuple: "+str(t))
l=list(t)
l[1]="z"
t=tuple(l)
print("Updated Tuple: "+str(t))























