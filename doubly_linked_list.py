class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Doublylinkedlist:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    
    def insertAtBeg(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return
        curr = self.head
        new_node.next = curr
        curr.prev = new_node
        self.head = new_node
    
    def insertAtInd(self, ind, val):
        if ind == 0:
            self.insertAtBeg(val)
            return
        if self.head is None:
            return
        curr = self.head
        while ind > 1 and curr is not None:
            curr = curr.next
            ind -= 1
        if curr is None:
            return
        new_node = Node(val)
        nxt = curr.next
        if nxt is None:
            curr.next = new_node
            new_node.prev = curr
            return
        curr.next = new_node
        new_node.prev = curr
        new_node.next = nxt
        nxt.prev = new_node



        