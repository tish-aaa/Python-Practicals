# Question:
# Define a function that computes the length of a given list or string. 


def leng(a):
    count=0
    for i in a:
        count+=1
    return count
a=input("Enter a string:")
print("Length of the string:",leng(a))

l=["pink","barbie","ken"]
print("List:",l)
print("Length of the list:",leng(l))



#a=len(Mylist)
#print("Length of list Mylist:",a)
#b='barbie'
#print("Length of string Barbie:",len(b))
