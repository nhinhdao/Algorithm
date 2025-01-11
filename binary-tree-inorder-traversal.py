# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.arr = []

    def inorderTraversalUsingRecursion(self, root):
        if root is None:
            return self.arr

        self.inorderTraversal(root.left)
        self.arr.append(root.val)
        self.inorderTraversal(root.right)

        return self.arr
    
    def inorderTraversal(self, root):
        stack = []
        node = root

        while stack or node:
            while node:
                # traverse left, append node to stack
                stack.append(node)
                node = node.left
            
            # end of left node (node is now NONE)
            node = stack.pop()
            self.arr.append(node.val)
            # traverse to right
            node = node.right

        return self.arr