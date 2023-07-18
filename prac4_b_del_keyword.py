# Question:
# Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements.

#manual input list
#this_list=[1,2,3,4,5,6,7,8]

#user-defined input list

this_list=[]
n=int(input("Enter the number of elements in the List:"))

print("Enter elements for the List:")
for i in range(0,n):
      a=input()
      this_list.append(a)
print("Original List:",this_list)

index=[0,2,4,5]
for i in sorted(index,reverse=True):
    del this_list[i]
    

print("Altered List:",this_list)

