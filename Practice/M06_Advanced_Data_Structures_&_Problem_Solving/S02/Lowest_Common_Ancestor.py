
''' Simple recursion approach(binary tree)
logic
1.if current node is none,return none
2.if current node is one of the target nodes (n1 or n2)
3.search in left subtree
4.search in right subtree
5.if both left and right return a node,current node is the LCA
6.otherwise return whichever side found a node'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#Tree structure  
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
def LCA(root,p,q):
    if root is None:
        return None
    if root.data == p or root.data==q:
        return root
    LCA(root.left,p,q)
    LCA(root.right,p,q)
    
print(LCA())