# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def find_p(self, node, p):
		if node is None:
			return False
		if node == p:
			return True
		return self.find_p(node.left, p) or self.find_p(node.right, p)


	def find_q(self, node, q):
		if node is None:
			return False
		if node == q:
			return True
		return self.find_q(node.left, q) or self.find_q(node.right, q)


	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		node = root
		while True:
			ret = node
			if self.find_p(node.left, p) and self.find_q(node.left, q):
				node = node.left
			elif self.find_p(node.right, p) and self.find_q(node.right, q):
				node = node.right
			else:
				return ret