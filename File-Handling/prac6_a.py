#Python program to read an entire text file.

#Creating a text file:
f=open("chandrayaan3.txt","x")

#Writing in the new text file:
f.write("Rover Pragyan surmounts its first Lunar obstacle, a 100mm-deep crater.")
f.close()

#open and read the file:
f = open("chandrayaan3.txt", "r")
print(f.read())
