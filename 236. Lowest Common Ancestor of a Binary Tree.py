# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def __init__(self):
		self.p_path = []
		self.q_path = []


	def dfs(self, node, tar, path):
		if node is None:
			return False
		path.append(node)
		if node == tar:
			return True
		if node.left is not None and self.dfs(node.left, tar, path):
			return True
		if node.right is not None and self.dfs(node.right, tar, path):
			return True
		path.pop()
		return False


	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		self.dfs(root, p, self.p_path)
		self.dfs(root, q, self.q_path)
		ret = None
		for i in range(min(len(self.p_path), len(self.q_path))):
			if self.p_path[i] == self.q_path[i]:
				ret = self.p_path[i]
			else:
				break
		return ret