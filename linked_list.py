class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBeg(self, data):
        val = Node(data)
        val.next = self.head
        self.head = val
    
    def insertAtEnd(self, data):
        val = Node(data)
        if self.head is None:
            self.head = val
        else:
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = val
    
    def insertAtInd(self, data, ind):
        curr = self.head
        count = 1
        new_data = Node(data)
        while (curr):
            curr = curr.next
            count += 1
            if count == ind:
                next_node = curr.next
                curr.next = new_data
                new_data.next = next_node
                break
            
    def deleteAtBeg(self):
        curr = self.head
        self.head = curr.next
    
    def deleteAtEnd(self):
        curr = self.head
        while (curr.next.next):
            curr = curr.next
        curr.next = None
    
    # def deleteAtInd(self, ind):
    #     curr = self.head
    #     count = 1
    #     while (curr):
    #         curr = curr.next
    #         count += 1
    #         if count == ind:
                
    def reverse(self):
        curr = self.head
        prev = None
        while (curr):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
            
    def display(self):
        val = self.head
        while val is not None:
            print(val.data, end=' -> ' if val.next else '')
            val = val.next

d = [3, 5, 10, 2, 7]
ll = LinkedList()
for j in d:
    ll.insertAtEnd(j)

# ll.insertAtInd(4, 3)
# ll.deleteAtEnd()
ll.display()
    
        






