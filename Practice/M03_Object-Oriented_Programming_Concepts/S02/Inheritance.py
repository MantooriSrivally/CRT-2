'''Inheritance:Accquering properties from parent class to child class
Reusability of code
1)parent class/base class/super class: having properties
2)child class/derived class/sub class
Types:
1)Single 🡺one parent🡪one child
2)Multi-level🡺chain formation{one grandparent🡪parent🡪child} a child class inherits from another child class
3)Multiple🡺multiple parent🡪one child
a child class inherits from more than one parent class
4)Hierarchical🡺one parent🡪multiple child
Multiple child classes inherit from same parent class
5)hybrid🡺combination of above all inheritance
Combination of two or more inheritance types
#single inheritance
class A:
    def display1(self):
        print("This is class A display method")
class B:
    def display2(self):
        print("This is class B display method")
b=B()
b.display1()
b.display2()
#multi-level inheritance
class A:
    def display1(self):
        print("This is class A display method")
class B:
    def display2(self):
        print("This is class B display method")
class C:
    def display3(self):
        print("This is Class B display method")
#hierarchical inheritance
class A:
    def display1(self):
        print("This is class A display method")
class B(A):
    def display2(self):
        print("This is class B display method")
class C(A):
    def display3(self):
        print("This is Class B display method")'''
#multiple inheritance
class A:
    def display(self):
        print("This is class A display method")
class B():
    def display(self):
        print("This is class B display method")
class C(A,B):
    def display3(self):
        print("This is Class B display method")
c=C()
c.display()
#MRO-method resolution order
