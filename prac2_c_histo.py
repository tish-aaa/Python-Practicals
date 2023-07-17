def histogram(n):
    for i in n:
        while i!=0:
            print("*",end="")
            i=i-1
        print()


histo=[4,9,7]
print("List:",histo)
histogram(histo)
