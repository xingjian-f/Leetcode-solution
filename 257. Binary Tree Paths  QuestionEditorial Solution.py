# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def __init__(self):
		self.ret = []


	def binaryTreePaths(self, root):
		if root is None:
			return []

		def dfs(node, path):
			path.append(str(node.val))
			if node.left is None and node.right is None:
				self.ret.append('->'.join(path))
			
			if node.left is not None:
				dfs(node.left, path)
			if node.right is not None:
				dfs(node.right, path)
			path.pop()


		dfs(root, [])
		return self.ret

# print Solution().binaryTreePaths([])