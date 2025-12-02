class maxHeap:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
        self.move_up(len(self.data)-1)
    
    def pop(self, index):
        if len(self.data) == 0:
            return -1
        self.data[index], self.data[-1] = self.data[-1], self.data[index]
        removed = self.data.pop()
        if index < len(self.data):
            self.move_up(index)
            self.move_down(index)
        return removed

    def move_up(self, index):
        parent = (index-1)//2
        if index > 0 and self.data[parent] < self.data[index]:
            temp = self.data[parent]
            self.data[parent] = self.data[index]
            self.data[index] = temp
            self.move_up(parent)
    
    def move_down(self, index):
        lc = (2*index)+1
        rc = (2*index)+2
        max_ind = index
        if lc < len(self.data) and self.data[lc] > self.data[max_ind]:
            max_ind = lc
        if rc < len(self.data) and self.data[rc] > self.data[max_ind]:
            max_ind = rc
        if max_ind != index:
            val = self.data[index]
            self.data[index] = self.data[max_ind]
            self.data[max_ind] = val
            self.move_down(max_ind)
    
    def heapify(self, arr):
        self.data = arr[:]
        start = len(self.data)//2-1
        for i in range(start, -1, -1):
            self.move_down(i)
    
    def heapSort(self):
        if len(self.data) == 0:
            return -1
        arr = []
        while self.data:
            arr.append(self.data[0])
            self.pop(0)
        return arr[::-1]

    def display(self):
        return self.data

obj = maxHeap()
arr = [1, 4, 10, 9, 3, 7, 100]
# for i in arr:
#     obj.push(i)
# obj.pop(2)
obj.heapify(arr)
print(obj.display())
print(obj.heapSort())