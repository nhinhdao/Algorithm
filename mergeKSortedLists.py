from printLinkedListValues import printVals

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        middle = len(lists)//2
        leftLists = lists[:middle]
        rightLists = lists[middle:]

        self.mergeKLists(leftLists)
        self.mergeKLists(rightLists)

        leftHead = leftLists[0] # head left
        rightHead = rightLists[0] # head right
        
        head = self.merge2SortedLists(leftHead, rightHead)
        return head
        
    
    def merge2SortedLists(self, left, right):
        head = ListNode()
        cur = head
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
                cur = cur.next
            else:
                cur.next = right
                right = right.next
                cur = cur.next

        while left:
            cur.next = left
            left = left.next
            cur = cur.next
        
        while right:
            cur.next = right
            right = right.next
            cur = cur.next

        return head.next
    



test = Solution()
nodeL2 = ListNode(5, None)
nodeL1 = ListNode(4, nodeL2)
left = ListNode(1, nodeL1)

nodeM2 = ListNode(4, None)
nodeM1 = ListNode(3, nodeM2)
middle = ListNode(1, nodeM1)

nodeR1 = ListNode(6, None)
right = ListNode(-1, nodeR1)

testcase = [left, middle, right]
head = test.mergeKLists(testcase)
printVals(head)