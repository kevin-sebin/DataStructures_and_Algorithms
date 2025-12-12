class Stack:
    def __init__(self, n):
        self.arr = []
        self.size = n
    
    def push(self, val):
        if not self.isFull():
            self.arr.append(val)
        else:
            print('stack is full')
    
    def pop(self):
        if not self.isEmpty():
            self.arr.pop(-1)
        else:
            print('stack is empty')
            
    def isEmpty(self):
        return len(self.arr) == 0

    def isFull(self):
        return len(self.arr) == self.size