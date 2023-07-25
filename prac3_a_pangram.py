string=input("Enter the sentence: ")
alp="abcdefghijklmnopqrstuvwxyz"
str1=string.lower()
flag=0
for char in alp:
    if char in str1:
        flag=0
    else:
        flag=1
        break
if flag==0:
    print("It is a Pangram.")
else:
    print("It is not a Pangram.")
            
