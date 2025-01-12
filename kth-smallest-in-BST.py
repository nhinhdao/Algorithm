# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k):
        if not root:
            return 0

        if k == 0:
            return root.val
        
        i = k
        arr = []
        res = []
        node = root

        while k > 0 or node:
            # traverse left tree to add number in acsending order in to arr
            while node:
                arr.append(node)
                node = node.left

            # hit the null node, pop the last node, which is also the smallest node
            node = arr.pop()

            # add the smallest val to the res array
            res.append(node.val)

            # set node to the right node
            node = node.right
            k -= 1
        
        return res[i-1]
        