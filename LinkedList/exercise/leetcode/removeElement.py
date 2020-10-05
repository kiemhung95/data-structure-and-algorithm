#
# remove linked list elements
# Input: 1 2 3 4 1 2 5, val: 1
# Output: 2 3 4 2 5
#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head
        while(current != None):
            print(current.data, end=' ')
            current = current.next

    def insertAtEnd(self, data):
        newNode = Node(data)
        current = self.head
        if(current is not None):
            while(current.next is not None):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

class Solution:
    def removeElement(self, linklist: LinkedList, val: int) -> LinkedList:
        prev = None
        current = linklist.head
        while(current is not None):
            if(current.data == val):
                if current is linklist.head:
                    linklist.head = linklist.head.next
                    prev = current
                    current = current.next
                elif current.next is None:
                    prev.next = None
                    current = current.next
                else:
                    prev.next = current.next
                    prev = prev if current.data == val else current
                    current = current.next
            else:
                prev = current
                current = current.next

        return linklist


# RUN

print("Input:")
linklist = LinkedList()
linklist.insertAtEnd(1)
linklist.insertAtEnd(2)
linklist.insertAtEnd(3)
linklist.insertAtEnd(4)
linklist.insertAtEnd(1)
linklist.insertAtEnd(5)
linklist.insertAtEnd(1)
linklist.printList()
print("\nOutput:")
solution = Solution()
solution.removeElement(linklist,1).printList()