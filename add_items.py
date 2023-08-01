#Adding items to tuple using 2 methods:
#1) Converting tuple to list and using append().
#2) Adding tuple to tuple.

print("Using append(): ")
t=(1,2,3,4)
l=list(t)
l.append(9)
t=tuple(l)
print(t)

print("Adding tuple to tuple: ")
t1=(100,99,98,97)
t2=("a","b")
t1+=t2
print(t1)
