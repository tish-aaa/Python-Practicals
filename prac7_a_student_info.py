# Design a class that store the information of student and display the same 

class student:
    def __init__(self) :
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.rollno = input("Enter RollNo: ")
        self.address = input("Enter Address: ")

    def disp(self):
        print("\nStudent Details:\nName: "+self.name+"\nAge: "+self.age)
        print("RollNo: "+self.rollno+"\nAddress: "+self.address)
        
# TO DISPLAY OBJECT IN STRING FORMAT
#     def __str__(self):
#         return f"{self.name} - {self.age} - {self.rollno} - {self.address}"
    
# S1 = student()
# print("Student Details:")
# print(S1)    

#CREATING OBJECT AND DISPLAY DETAILS
S1 = student()
S1.disp()

