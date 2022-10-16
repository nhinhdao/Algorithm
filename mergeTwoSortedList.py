# Definition for singly-linked list.
from multiprocessing import Array


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # 1   .2   3
        # 1   3   5   6   7
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
            tail = tail.next
        
        else:
            tail.next = list2
        
        head = dummy.next
        dummy.next = None

        return head

def printLinkListValues(list):
    arr = []
    while list:
        arr.append(list.val)
        list = list.next
    
    print(arr)


node3 = ListNode(3, None)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

node5 = ListNode(5, None)
node3b = ListNode(3, node5)
node1b = ListNode(1, node3b)

sol = Solution()
newList = sol.mergeTwoLists(node1, node1b)
printLinkListValues(newList)
