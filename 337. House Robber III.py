# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def __init__(self):
		self.dp = {}


	def dfs(self, root, ok):
		if root is None:
			return 0
		if (root, ok) in self.dp:
			return self.dp[(root, ok)]
		ret = 0
		if ok:
			ret = max(ret, root.val + self.dfs(root.left, False) + self.dfs(root.right, False))
		ret = max(ret, self.dfs(root.left, True) + self.dfs(root.right, True))
		self.dp[(root, ok)] = ret
		return ret


	def rob(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		return self.dfs(root, True)