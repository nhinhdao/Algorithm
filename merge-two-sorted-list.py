# Definition for singly-linked list.
from multiprocessing import Array


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        head = list1 if list1 and list2 and list1.val <= list2.val else list1


        while list1 and list2:
            next1 = list1.next
            next2 = list2.next

            if list1.val <= list2.val:
                list1.next = list2
                list1 = next1
            else:
                list2.next = list1
                list2 = next2

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
