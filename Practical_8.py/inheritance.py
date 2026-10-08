### single inheritance 

class parent:
    def show_parent(self):
        print("This is parent class")
class child(parent):
    def show_child(self):
        print("This is child class")
        
obj = child()
obj.show_parent()
obj.show_child()


### multiple inheritance

class Father:
    def father(self):
        print("This is a father of child")
class Mother:
    def mother(self):
        print("This is a mother of child")
class Child(Father,Mother):
    def child(self):
        print(" I'm a child ")
obj = Child()
obj.father()
obj.mother()
obj.child()


### multilevel inheritance 

class Grandparent:
    def grandparent(self):
        print("This is Grandparent class")

class Parent(Grandparent):
    def parent(self):
        print("This is Parent class")

class Child(Parent):
    def child(self):
        print("This is Child class")

obj = Child()
obj.grandparent()
obj.parent()
obj.child()


### hierarchical inheritance

class Parent:
    def parent(self):
        print("This is Parent class") 

class Child1(Parent):
    def child1(self):
        print("This is Child1 class")

class Child2(Parent):
    def child2(self):
        print("This is Child2 class")

obj1 = Child1()
obj2 = Child2()

obj1.parent()
obj1.child1()

obj2.parent()
obj2.child2()

### hybrid inheritance 
class A:

    def show_a(self):
        print("This is main class A")


class B(A):

    def show_b(self):
        print("This is child1 of class A")


class C(A):

    def show_c(self):
        print("This is child2 of class A")


class D(B, C):

    def show_d(self):
        print("This is child of class B and class C")


obj = D()

obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()