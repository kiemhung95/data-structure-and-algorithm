#
# Write a Python program to search a specific item in a singly linked list 
# and return true if the item is found otherwise return false.
#

class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end=' ')
            temp = temp.next

    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        if temp != None:
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
        else:
            self.head = newNode

    def isNodeExist(self, data):
        temp = self.head
        isExist = False
        while(temp != None):
            if(temp.data == data):
                isExist = True
                break
            else:
                temp = temp.next
        
        return isExist

linkedlist = LinkedList()
linkedlist.insertAtEnd(1)
linkedlist.insertAtEnd(2)
linkedlist.insertAtEnd(3)
linkedlist.printList()
print(linkedlist.isNodeExist(1))
print(linkedlist.isNodeExist(2))
print(linkedlist.isNodeExist(3))
print(linkedlist.isNodeExist(4))