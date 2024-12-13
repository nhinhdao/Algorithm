class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Implementation for Doubly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with 'dummy' head and tail nodes which makes 
        # edge cases for insert & remove easier.
        self.head = ListNode(1)
        self.tail = ListNode(1000)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insertFront(self, val):
        curr = self.head
        self.head = ListNode(val)
        self.head.next = curr
        curr.prev = self.head

    def insertEnd(self, val):
        newNode = ListNode(val)
        lastNode = self.tail
        self.tail.next = newNode
        self.tail.next.prev = lastNode 

    # Remove first node after dummy head (assume it exists)
    def removeFront(self):

    # Remove last node before dummy tail (assume it exists)
    def removeEnd(self):

    def print(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, " -> ")
            curr = curr.next
        print()