#
# Write a Python program to find the size of a singly linked list
#

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def append_item(self, data):
        newNode = Node(data)
        temp = self.head
        if temp:
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
        else:
            self.head = newNode

        self.count += 1

linkedList = LinkedList()
linkedList.append_item(1)
linkedList.append_item(1)
linkedList.append_item(1)
linkedList.append_item(1)
linkedList.append_item(1)
linkedList.append_item(1)
linkedList.append_item(1)
linkedList.append_item(1)
linkedList.append_item(1)
linkedList.append_item(1)
linkedList.append_item(1)
print(linkedList.count)