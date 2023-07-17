# Question:
# Write a program to generate the Fibonacci series.

n=int(input("Enter the limit:"))
n1=0
n2=1
print("Fibonacci Series:")
print(n1)
while n!=0:
    a=n1+n2
    print(a)
    n1=n2
    n2=a
    n=n-1   


