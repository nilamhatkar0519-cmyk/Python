class Student:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Constructor is called..")
        
    def display(self):
        print("Name :" , self.name)
        print("Age :", self.age)
        
    def __del__(self):
        print("Destructor is called..")


name = input("Enter name : ")
age = int(input("Enter age : "))
s = Student(name,age)
s.display()
# call the destructor 
#del s 


## super() function 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def display_student(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

name = input("Enter name: ")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

s = Student(name, age, marks)
s.display_student()