class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def getHeight(self, node):
        return node.height if node else 0
    
    def getBalanceFactor(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right)

    def insert(self, val):
        curr = self.root
        def dfs(node, val):
            if node is None:
                return treeNode(val)
            if node.val > val:
                node.left = dfs(node.left, val)
            elif node.val < val:
                node.right = dfs(node.right, val)
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            bf = self.getBalanceFactor(node)
            if bf > 1:
                if node.left.val > val:
                    node = self.rightRotate(node)
                else:
                    node.left = self.leftRotate(node.left)
                    node = self.rightRotate(node)
            elif bf < -1:
                if node.right.val < val:
                    node = self.leftRotate(node)
                else:
                    node.right = self.rightRotate(node.right)
                    node = self.leftRotate(node)

            return node
        self.root = dfs(self.root, val)
    
    def leftRotate(self, node):
        rc = node.right
        rc_left = rc.left
        rc.left = node
        node.right = rc_left
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        rc.height = 1 + max(self.getHeight(rc.left), self.getHeight(rc.right))
        return rc
    
    def rightRotate(self, node):
        lc = node.left
        lc_right = lc.right
        lc.right = node
        node.left = lc_right
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        lc.height = 1 + max(self.getHeight(lc.left), self.getHeight(lc.right))
        return lc

    def display(self):
        if not self.root:
            return
        queue = [[self.root]]
        fin = [[self.root.val]]
        while queue:
            ele = queue[-1]
            sub = []
            vals = []
            for i in ele:
                if i.left:
                    sub.append(i.left)
                    vals.append(i.left.val)
                if i.right:
                    sub.append(i.right)
                    vals.append(i.right.val)
            if sub:
                queue.append(sub)
                fin.append(vals)
            else:
                break
        return fin


avl = AVLTree()
arr = [5, 6, 2, 3, 9, 10, 8]
for i in arr:
    avl.insert(i)
print(avl.display())

            

