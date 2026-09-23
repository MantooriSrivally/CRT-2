'''Type checking: To check the value of particular type()'''
a=10
b=5.6
c="Vally"
d=[1,2,3,4,5]
e=(1,2,3,4,5)
f={1,2,3,4,5}
g={"name": "Vally"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

'''
isinstance():to check the value/object is belongs to particular class or datatype
syntax:
isinstance(obj,type)
it gives us boolean value(True/False)
'''
a=10
b=5.6
c="Vally"
d=[1,2,3,4,5]
e=(1,2,3,4,5)
f={1,2,3,4,5}
g={"name": "Vally"}
print(isinstance(a,int))
print(isinstance(b,float))
print(isinstance(c,str))
print(isinstance(d,set))
print(isinstance(e,set))
print(isinstance(f,tuple))
print(isinstance(g,dict))