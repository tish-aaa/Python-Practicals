#Remove an item from a Tuple.
#Converting to list and using remove().

t=(1,2,3,4)
print("Original Tuple: "+str(t))
l=list(t)
l.remove(3)
t=tuple(l)                                                                            
print("Altered Tuple: "+str(t))
