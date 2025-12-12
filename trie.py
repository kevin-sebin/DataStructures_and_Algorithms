class Node:
    def __init__(self):
        self.count = 0
        self.arr = [0]*26
        self.end = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def insertWord(self, word):
        curr = self.root
        for c in word:
            pos = (ord(c)-ord('a'))%26
            if curr.arr[pos] == 0:
                curr.arr[pos] = Node()
            curr = curr.arr[pos]
        curr.end = 1
        curr.count += 1

    def searchWord(self, word):
        curr = self.root
        for i in word:
            pos = (ord(i)-ord('a'))%26
            if curr.arr[pos] == 0:
                return False
            curr = curr.arr[pos]
        return curr.end == 1

    def commonPrefix(self, pre):
        curr = self.root
        prefix = ''
        for i in pre:
            pos = (ord(i)-ord('a'))%26
            if curr.arr[pos] == 0:
                return False
            prefix += i
            curr = curr.arr[pos]
        words = []
        def dfs(node, string):
            if node.end == 1:
                words.append(string)
            for j in range(26):
                if node.arr[j] != 0:
                    dfs(node.arr[j], string+chr(ord('a')+j))
        dfs(curr, prefix)
        return words if len(words) >= 1 else []

    def display(self):
        return self.root.arr
    
obj = Trie()
obj.insertWord('apple')
obj.insertWord('nigger')
obj.insertWord('apples')
obj.insertWord('app')
print(obj.display())



