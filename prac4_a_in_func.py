# Question:
# Write a program that takes two lists and returns True if they have at least one common member.

#manual lists 
#list1=[1,2]
#list2=[1,2,4,5,6,7]

#user-defined inputs
list1=[]
list2=[]

n=int(input("Enter the number of elements in List1:"))

print("Enter elements for List1:")
for i in range(0,n):
      a=input()
      list1.append(a)
print("List1:",list1)

m=int(input("Enter the number of elements in List2:"))
print("Enter elements for List2:")
for i in range(0,m):
      b=input()
      list2.append(b)
print("List2:",list2)


temp=0
for i in list1:
    if i in list2:
        temp=temp+1

if temp>0:
    print("TRUE")
else:
    print("FALSE")
        
