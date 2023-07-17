# Question:
# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

def vowel(a):
    if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
        print("True. It is a vowel.")
    else:
        print("False. It is a consonant.")

a=input("Enter a character:")
vowel(a)
