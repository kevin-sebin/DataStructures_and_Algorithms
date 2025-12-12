class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self):
        self.root = None
    
    def buildTree(self, val):
        curr = self.root
        if not curr:
            self.root = Node(val)
            return
        def dfs(node, val):
            if node is None:
                return Node(val)
            if node.val > val:
                node.left = dfs(node.left, val)
            if node.val < val:
                node.right = dfs(node.right, val)
            return node
        self.root = dfs(self.root, val)
    
    def inOrderTraversal(self, root, arr):
        if not root:
            return
        self.inOrderTraversal(root.left, arr)
        arr.append(root.val)
        self.inOrderTraversal(root.right, arr)
        return arr
    
obj = binarySearchTree()
arr = [5, 3, 1, 9, 10, 7, 6, 4, 3, 9, 11]
for i in arr:
    obj.buildTree(i)
print(obj.inOrderTraversal(obj.root, []))

        
            
            
