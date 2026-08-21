from my_package.marks import total
from my_package.student import display 

name = input("Enter your name : ")
a = int(input("Enter marks of sub1 : "))
b = int(input("Enter marks of sub2 : "))
c = int(input("Enter marks of sub3 : "))

display(name)
print("Total marks : ", total(a,b,c))
print("Avg of marks : ",(total(a,b,c)/3))
