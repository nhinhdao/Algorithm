class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def reverseList(self, head):
        # first node point to second node => second point to first
        # second points to third => third points to second
        # variable for: first node, second node and the third node
        # currentNode = head
        # leftNode = null (head dont have left node)
        # rightNode = head.next

        prevNode = None
        currentNode = head

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode