from collections import deque
import queue

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

def BFS(node):
    if node is None:
        return
    d = deque()
    d.append(node)
    while d:
        current_node = d.popleft()
        print(current_node.data, end="-->")
        if current_node.left:
            d.append(current_node.left)
        if current_node.right:
            d.append(current_node.right)

BFS(root)