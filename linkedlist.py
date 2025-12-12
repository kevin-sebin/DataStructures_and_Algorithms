class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node
    
    def insertAtBeg(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            new_node.next = curr
            self.head = new_node
    
    def insertAtInd(self, ind, nd):
        new_node = Node(nd)
        if self.head is None:
            print('list is empty')
        elif self.head.next is None:
            if ind == 0:
                self.insertAtBeg(new_node)
            elif ind == 1:
                self.insertAtEnd(new_node)
            else:
                print('index out of range')
        else:
            count = 1
            curr = self.head
            while (count != ind):
                curr = curr.next
                count += 1
            temp = curr.next.next
            new_node.next = temp
            curr.next = new_node
    
    def deleteAtEnd(self):
        if self.head is None:
            print('list already empty')
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while (temp.next.next):
                temp = temp.next
            temp.next = None

    def deleteAtBeg(self):
        if self.head is None:
            print('list is empty')
        elif self.head.next is None:
            self.head = None
        else:
            move = self.head
            self.head = self.head.next
            move = None
    
    def hasCycle(self):
        if not self.head:
            return
        if not self.head.next:
            return False
        curr = self.head
        a, b = curr, curr
        while (a.next or b.next):
            if not a.next:
                a = a.next.next
                b = b.next
                if a == b:
                    return True
            else:
                break
        return False

    def displayReverse(self):
        if self.head is None:
            print('list is empty')
        elif self.head.next is None:
            print(self.head)
        else:
            stack = []
            curr = self.head
            while (curr):
                stack.append(curr.data)
                curr = curr.next
            for i in range(len(stack)):
                print(stack.pop())

    def display(self):
        curr = self.head
        while(curr):
            print(curr.data, end='->')
            curr = curr.next
        print('\n')
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

ll = LinkedList()
for i in range(5):
    ll.insertAtBeg(i)
print(ll.hasCycle())
ll.display()

# ll.insertAtInd(3, 99)
# ll.display()


