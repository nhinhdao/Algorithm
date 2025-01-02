# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def insertIntoBSTRecursive(self, root, val):
        """
        base case
        if no root:
            return Treenode(val)

        - compare node.val to val
        - if node.val < val:
            root.left = insertIntoBST(root.left, val)
        - if root.val > val:
            root.right = insertIntoBST(root.right, val)
        return root
        """
        if root is None:
            return TreeNode(val)
        
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root
    
    def insertIntoBST(self, root, val):
        '''
        - same base case
        - set a node = root
        - travel down and reset root
            while node:
                temp = node
                if node.val > val
                    node = node.left
                else:
                    node = node.right
            
        - get to the end of tree branch
        - create a new node
        - compare value of newnode and val to set left or right
        '''
        newNode = TreeNode(val)

        if root is None:
            return newNode

        node = root

        while node:
            temp = node
            if node.val > val:
                node = node.left
            else: 
                node = node.right
        
        if temp.val > newNode.val:
            temp.left = newNode
        else:
            temp.right = newNode

        
        return root
        