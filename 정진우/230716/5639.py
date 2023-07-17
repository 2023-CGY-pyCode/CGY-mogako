import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

class Tree:
    def __init__(self):
        self.root = None
        
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def bst(new_node, node):
    if new_node.value < node.value:
        if node.left is not None:
            bst(new_node, node.left)
        else:
            node.left = new_node
    else:
        if node.right is not None:
            bst(new_node, node.right)
        else:
            node.right = new_node
            
def post_order(node):
    if node is None:
        return 
    post_order(node.left)
    post_order(node.right)
    
    print(node.value)
    return
    
tree = Tree()
li = []
while True:
    try:
        node = Node(int(input()))
        if not tree.root:
            tree.root = node
        else:
            li.append(node)
    except:
        root = tree.root    
        for i in li:
            bst(i, root)
        post_order(root)
        break
        