'''#single inheritance
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
'''class A:
    def display(self):
        print("This is class A display method")
class B():
    def display(self):
        print("This is class B display method")
class C(A,B):
    def display3(self):
        print("This is Class B display method")
c=C()
c.display()'''
'''polymorphism:
pol-->many
morph-->forms

Types of polymorphism:
1.complie-time
    1.function overloading-crating multiple functions
    2.Operator overloading
2.Run-time
    1.Method overriding '''
#type checking
'''a=10
print(type(a))
#checking multiple values
x="Vally"
if isinstance(x,(int,float)):
    print("Given x is int or float")
else:
    print("Given x is a string")
#checking with classes
class Animal:
    pass
class Dog(Animal):
    pass
class cat:
    pass
d=Dog()
c=cat()
print(isinstance(d,Dog))
print(isinstance(d,Animal))
print(isinstance(c,Dog))
print(isinstance(c,cat))
#duck typing:same method acts as same behaviour ,we can use it 
class Dog:
    def sound(self):
        print("Bow-Bow")
class Cat:
    def sound(self):
        print("Meow-Meow")
def make_sound(animal):
    animal.sound()
d=Dog()
c=Cat()
make_sound(d)
make_sound(c)
def process(data):
    if isinstance(data,int):
        return data*2
    elif isinstance(data,str):
        return data.upper()
    elif isinstance(data,float):
        return data*10.5
print(process(10))
print(process('vally'))
print(process(10.56))'''
#interview question
class A:
    pass
class B:
    pass
obj=B()
print(type(obj)==B)  #output:True
print(type(obj)==A)  #output:false
print(isinstance(obj,B))  #output:True
print(isinstance(obj,A))  #output:false