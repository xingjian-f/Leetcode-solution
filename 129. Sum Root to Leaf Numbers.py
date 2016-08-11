# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def __init__(self):
		self.ans = 0

	def dfs(self, root, path):
		if root.left is None and root.right is None:
			print path
			self.ans += int(''.join(map(str,path)))
		if root.left is not None:
			path.append(root.left.val)
			self.dfs(root.left, path)
			path.pop()
		if root.right is not None:
			path.append(root.right.val)
			self.dfs(root.right, path)
			path.pop()


	def sumNumbers(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root is not None:
			self.dfs(root, [root.val])
		return self.ans