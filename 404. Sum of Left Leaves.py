# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def dfs(self, node, left):
		if node is None:
			return 0
		if node.left is None and node.right is None and left:
			return node.val
		ret = 0
		if node.left is not None:
			ret += self.dfs(node.left, True)
		if node.right is not None:
			ret += self.dfs(node.right, False)
		return ret 


	def sumOfLeftLeaves(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		return self.dfs(root, False)