class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=', ')
    inOrderTraversal(node.right)

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=', ')

def breadthFristTraversal(node):
    root = node
    queue = []
    queue.append(root)
    while queue: 
        new_curr = queue[0]
        print(new_curr.data, end=', ')
        del queue[0]
        if new_curr.left:
            queue.append(new_curr.left)
        if new_curr.right:
            queue.append(new_curr.right)

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print(breadthFristTraversal(root))