class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def Height(root):
    if root is None:
        return -1

    l = Height(root.left)
    r = Height(root.right)

    return 1 + max(l, r)

def Diameter(root):
    if root is None:
        return 0

    l = Height(root.left)
    r = Height(root.right)

    d = l + r + 2

    d_l=Diameter(root.left)
    d_r=Diameter(root,right)
    return max(d,d_l,d_r)

print(Diameter(root))


