'''Double Linked List:
the data can be store in the nodes
nodes-->3 parts
1.data
2.prev
3.next'''
''' Algorithm:
1. Create a node
2. Insert a node 
3. Connection
4. Traversal
'''

class Node:
    def _init_(self, data):
        self.data = data
        self.prev = None
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
# Connection
node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2  

node3.next = node4
node4.prev = node3

def traverse():
    current = node1
    while current:
        print(current.data,end=" <-> ")
        current = current.next
print()
traverse()
[9:51 am, 23/09/2026] +91 91215 02006: #write the code to print in reverse order
def traverse_reverse():
    current = node4
    while current:
        print(current.data,end=" <-> ")
        current = current.prev
    print("None")
traverse_reverse




#insertion of a node at the beginning
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def insert_begin(head,data):
    new_node=Node(data)
    new_node.next=head
    if head:
        head.prev=new_node
    return new_node      
def insertion_end(head,data):
    new_node=Node(data)
    if head is None:
        return new_node
    curr=head
    while curr.next:
        curr=curr.next
    curr.next=new_node
    new_node.prev=curr.next
    return head
def traverse(head):
    curr=head
    while curr:
        print(curr.data,end="<->")
        curr=curr.next
    print("None")
head=None
head=insert_begin(head,50)
head=insert_begin(head,60)
head=insert_begin(head,70)
print("Insertion at the Begin")
traverse(head)
print()  