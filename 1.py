
class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def showdata(self):
        print("Name :",self.name)
        print("Roll no:",self.rollno)

s1=student(input("Enter the name:"),int(input("Enter the roll no:")))
s2=student(input("Enter the name:"),int(input("Enter the roll no:")))
print("Student 1:")
s1.showdata()
print("Student 2:")
s2.showdata()
