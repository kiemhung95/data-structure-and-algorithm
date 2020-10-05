#
# Write a Python program to create a singly linked list, append some items and iterate through the list.
#

class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def interation_list(self):
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

    def append_item(self, data):
        newNode = Node(data)
        temp = self.head
        if temp:
            while (temp.next != None):
                temp = temp.next
            temp.next = newNode
        else:
            self.head = newNode

        #print(self.head)
               
linkedList = LinkedList()
linkedList.append_item(1)
linkedList.append_item(2)
linkedList.append_item(2)
linkedList.append_item(2)
linkedList.append_item(2)
linkedList.append_item(2)
print(linkedList.printList())
for val in linkedList.interation_list():
    print(val)
