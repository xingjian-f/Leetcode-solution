# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def dfs1(self, node, tar):
		ret = self.dfs(node, tar)
		if node.left is not None:
			ret += self.dfs1(node.left, tar)
		if node.right is not None:
			ret += self.dfs1(node.right, tar)
		return ret 


	def dfs(self, node, tar):
		ret = 0
		if node.val == tar:
			ret += 1
		if node.left is not None:
			ret += self.dfs(node.left, tar-node.val)
		if node.right is not None:
			ret += self.dfs(node.right, tar-node.val)		
		
		return ret


	def pathSum(self, root, tar):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: int
		"""
		if root is None:
			return 0
		ret = self.dfs1(root, tar)
		return ret