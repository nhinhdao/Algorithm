class Solution(object):
    def searchBSTRecursive(self, root, val):
        """
        - start at root
        root.val < val go search root.right
        root.val > val search root.left
        """
        if root is None:
            return None
        
        if root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return root
        
        return None
    
    def searchBST(self, root, val):
        if root is None:
            return None

        node = root
        while node:
            if node.val > val:
                node = node.left
            elif node.val < val:
                node = node.right
            else:
                break
        
        return node if node and node.val == val else None