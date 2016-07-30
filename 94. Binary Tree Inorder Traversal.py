# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ret = []
        if root is not None:
        	stack.append((root, 0))
        while len(stack)>0:
        	top = stack.pop()
        	node, tag = top[0], top[1]
        	val = node.val
        	left = node.left
        	right = node.right
        	if tag == 1:
        		ret.append(val)
        	else:
        		if right is not None:
        			stack.append((right, 0))
        		stack.append((node, 1))
        		if left is not None:
        			stack.append((left, 0))

        return ret