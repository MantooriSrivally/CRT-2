#Stack implementation using  list
class Stack:
    def __init__(self):
        self.s=[]
    def push(self,val):
        self.s.append(val)
    def is_empty(self):
        return len(self.s)==0
        '''if len(self.s)==0:
            return True
        else:
            return False'''
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.s.pop()
    def size(self):
        return len()

    def peek(self):
        pass
        

st=Stack()
print(st.is_empty())#true
st.push(10)
st.push(20)
st.push(30)
print(st.is_empty())#false
print(st.pop())#30
print(st.size())#2
print(st.peek())#20
#Stack implementation using Linked list
class Node:
    pass
class Stack_LL:
    def __init__(self):
        self.top=None
    def push(self,val):
        new_node=Node(val)
        new_node.next=self.top
        self.top=new_node
    def is_empty(self):
        return self.top is None
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        del_val=self.top.data
        self.top=self.top.next
        return del_val
    def size(self):
        temp=self.top
        count=0
        

