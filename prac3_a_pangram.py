#Question:
#A pangram is a sentence that contains all the letters of the English alphabet at least once, 
#for example: The quick brown fox jumps over the lazy dog. . Your task here is to write a 
#function to check a sentence to see if it is a pangram or not.

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
            
