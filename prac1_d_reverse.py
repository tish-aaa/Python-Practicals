# Question:
# Write a function that reverses the user defined value.


n=int(input("Enter the number:"))
rev=0
while n != 0:
    r=n%10
    rev=rev*10+r
    n//=10
print("Reversed Number:",rev)
    
