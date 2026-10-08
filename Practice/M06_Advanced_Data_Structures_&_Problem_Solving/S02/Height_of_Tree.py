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

def height(node):
    if node is None:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1

print("Height of the tree:", height(root))