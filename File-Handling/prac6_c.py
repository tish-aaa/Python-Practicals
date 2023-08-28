#Python program to read last n lines of a file.


n=int(input("Enter the number of lines you want to read:"))
f=open("chandrayaan3.txt","r")
#for x in f:
#    print(f.readlines(n))
#    n=n-1
#f.close()

for line in (f.readlines() [-n:]):
    print(line, end ='')
f.close()
