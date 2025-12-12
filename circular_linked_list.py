class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeg(self, data):
        new_node = Node(data)
        curr = self.head
        if curr is None:
            self.head = new_node
            new_node.next = self.head
        elif curr.next is None:
            new_node.next = curr
            self.head = new_node
            self.head.next.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            while (curr):
                curr = curr.next
            curr.next = self.head
        
    def display(self):
        curr = self.head
        while (curr):
            print(curr.data)
            curr = curr.next
        print('\n')