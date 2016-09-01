# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def __init__(self):
		self.idx = 0
		self.res = None


	def dfs(self, node, k):
		if node.left is not None:
			self.dfs(node.left, k)
		self.idx += 1
		if self.idx == k:
			self.res = node.val
			return
		if node.right is not None:
			self.dfs(node.right, k)


	def kthSmallest(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		self.dfs(root, k)
		return self.res