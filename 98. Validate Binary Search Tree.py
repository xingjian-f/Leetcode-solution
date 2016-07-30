# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def __init__(self):
		self.dpmin = {}
		self.dpmax = {}

	def findmin(self, root):
		if root in self.dpmin:
			return self.dpmin[root]
		ret = root.val
		if root.left is not None:
			ret = min(ret, self.findmin(root.left))
		if root.right is not None:
			ret = min(ret, self.findmin(root.right))
		self.dpmin[root] = ret
		return ret

	def findmax(self, root):
		if root in self.dpmax:
			return self.dpmax[root]
		ret = root.val
		if root.left is not None:
			ret = max(ret, self.findmax(root.left))
		if root.right is not None:
			ret = max(ret, self.findmax(root.right))
		self.dpmax[root] = ret
		return ret

	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if root is None:
			return True
		ret = True
		if root.left is not None:
			ret = ret and self.findmax(root.left) < root.val and self.isValidBST(root.left) 
		if root.right is not None:
			ret = ret and self.findmin(root.right) > root.val and self.isValidBST(root.right)
		return ret