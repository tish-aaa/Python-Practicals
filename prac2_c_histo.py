# Question:
# Define a procedure histogram() that takes a list of integers and prints a histogram to the 
# screen. For example, histogram([4, 9, 7])should print the following: 
# ****
# ********
# ****

def histogram(n):
    for i in n:
        while i!=0:
            print("*",end="")
            i=i-1
        print()


histo=[4,9,7]
print("List:",histo)
histogram(histo)
