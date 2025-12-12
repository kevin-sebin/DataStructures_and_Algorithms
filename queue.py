class Queue:
    def __init__(self, size):
        self.arr = []
        self.size = size
    
    def isFull(self):
        if len(self.arr) == self.size:
            return True
        return False

    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        return False
    
    def enqueue(self, val):
        if not self.isFull():
            self.arr.append(val)
        else:
            print('queue is full')
        
    def dequeue(self):
        if not self.isEmpty:
            self.arr.pop()
        else:
            print('queue is empty')
        
    def display(self):
        for i in self.arr:
            print(i, end=' ')
        print('\n')

queue = Queue(5)
for i in range(5):
    queue.enqueue(i)
queue.display()
queue.dequeue()
queue.display()

