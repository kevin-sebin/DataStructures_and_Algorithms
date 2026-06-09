class bloomFilter:
    def __init__(self, length=1000, k=3):
        self.length = length
        self.k = k
        self.arr = [0]*self.length
    
    def hashFunction(self, item):
        h1 = hash('seed' + item)
        h2 = hash('seed' + item)
        for i in range(self.k):
            yield (h1 + i*h2)% self.length
    
    def add(self, item):
        for pos in self.hashFunction(item):
            self.arr[pos] = 1
    
    def check(self, item):
        for pos in self.hashFunction(item):
            if self.arr[pos] == 0:
                return False
        return True
    

obj = bloomFilter()
while True:
    inp = input(": ")
    if not obj.check(inp):
        print("adding:", inp)
        obj.add(inp)
    else:
        print("probably already exists")
        