# Question:
# Write a Python program to clone or copy a list .


list1=[]
clonedlist=[]

n=int(input("Enter the number of elements in the List:"))
print("Enter the elements of the List:")
for i in range(0,n):
    a=input()
    list1.append(a)
print("Original List:",list1)

clonedlist.extend(list1)
print("Cloned List:",clonedlist)
