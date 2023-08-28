#Python program to append text to a file and display the text.

f=open("chandrayaan3.txt","a")
f.write("\nNew Update: Currently, the only active rover on the lunar surface besides India's is China's Yutu 2 rover, sent by Chang’e 4.")
f.close()

f=open("chandrayaan3.txt","r")
print(f.read())
