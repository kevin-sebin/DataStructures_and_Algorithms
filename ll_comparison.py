class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    def hasCycle(self, head:None):
        curr = self.head
        B, b = curr, curr
        flag = False
        while (curr):
            B = curr.next.next
            b = curr.next
            if B == b:
                flag = True
                break
            else:
                flag = False
        return flag

    def insertAtBeg(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            new_node.next = curr
            self.head = new_node

    def returnHead(self):
        return self.head

    def display(self):
        curr = self.head
        while(curr):
            print(curr.val, end=' -> ')
            curr = curr.next
        print('\n')

d = [1, 2, 3, 4, 5]
ll = Solution()
for i in d:
    ll.insertAtBeg(i)
print(ll.hasCycle(ll.returnHead()))
ll.display()