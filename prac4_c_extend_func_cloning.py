list1=[]
clonedlist=[]

n=int(input("Enter the number of elements in List1:"))
print("Enter the elements of List1:")
for i in range(0,n):
    a=input()
    list1.append(a)
print("List:",list1)

clonedlist.extend(list1)
print("Cloned List:",clonedlist)
