def armstrong(n):
   a=n
   c=0
   while n!=0:
      n//=10
      c+=1
   n=a
   arm=0
   while n!=0:
      r=n%10
      arm=arm+r**c
      n//=10
   if arm==a:
      print(a,"is an Armstrong Number.")
   else:
      print(a,"is not an Armstrong Number.")
   
   
n=int(input("Enter a number for Armstrong:"))
armstrong(n)



def palindrome(z):
   sum=0
   x=z
   while z!=0:
     r=z%10
     sum=sum*10+r
     z//=10
   if x==sum:
       print(x,"is a Palindrome.")
   else:
       print(x,"is not a Palindrome.")

z=int(input("Enter a number for Palindrome:"))
palindrome(z)
