this_list=[1,2,3,4,5,6,7,8]
print("Original List:",this_list)

index=[0,2,4,5]
for i in sorted(index,reverse=True):
    del this_list[i]
    

print("Altered List:",this_list)

