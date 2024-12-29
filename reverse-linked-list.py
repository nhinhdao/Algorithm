class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def reverseList(self, head):
        start = None
        curr = head

        while curr:
            next = curr.next
            curr.next = start
            start = curr
            curr = next
        
        return start

    def reverseListUsingRecursion(self, head):

        def reverseWithRecursion(node1, node2):
            # basecase
            # when the nextNode is None, we hit the end of the linked list
            # turn the node before the nextNode
            if node2 is None:
                return node1

            # keep track of next node after node2
            nextNode = node2.next

            # point node2 back to node1
            node2.next = node1

            # continue reverse node2 and nextNode
            return reverseWithRecursion(node2, nextNode)

        

        return reverseWithRecursion(None, head)



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
test.reverseList(node1)
print(test.reverseListUsingRecursion(node1).val)