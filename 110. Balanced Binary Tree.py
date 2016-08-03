# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def max_depth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        ret = 0
        if root.left is not None:
            ret = max(ret, self.max_depth(root.left)+1)
        if root.right is not None:
            ret = max(ret, self.max_depth(root.right)+1)
        return ret
        
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return abs(self.max_depth(root.left)-self.max_depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
        