class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

root = Node(10)
root.left = Node(20)
root.left.left = Node(30)
root.right = Node(40)
root.right.left = Node(50)

postorder(root)
