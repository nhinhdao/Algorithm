class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

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

    def reverseListUsingRecursion(self, head):        
        """
        1. Simple inputs
        1 -> None :
        r: 1 -> None

        1 -> 2 -> None
        2 -> 1 -> None = 2 -> reverse(1)

        1 -> 2 -> 3 -> None
        3 -> 2 -> 1 -> None =  3 -> reverse(2)

        2. Pattern
        get the next node from the argument node
        set the next of the current node to prev node
        now reverse current node and the next node until it is None
        """
        def reverse(prev, curr):
            if curr is None:
                return prev
            next = curr.next
            curr.next = prev

            return reverse(curr, next)
        
        return reverse(None, head)

    def factorial(self, num): #1
        if num == 1:
            return num
        
        next = self.factorial(num-1)

        return num * next
        # 5 * 1 = 5


node4 = ListNode(4, None)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
test = LinkedList()
print(test.reverseListUsingRecursion(node1).val)