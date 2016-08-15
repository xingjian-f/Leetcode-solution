# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        if root is not None:
        	stack.append(root)
        ret = []
        while len(stack) > 0:
        	top = stack.pop()
        	ret.append(top.val)
        	if top.right is not None:
        		stack.append(top.right)
        	if top.left is not None:
        		stack.append(top.left)
        return ret