# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def dfs(self, node, x, height):
		if height == 1:
			if node is None:
				return False
			else:
				return True
		if x <= 2 ** (height-2):
			return self.dfs(node.left, x, height-1)
		else:
			return self.dfs(node.right, x-2 ** (height-2), height-1)


	def countNodes(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		height = 0
		node = root
		while node is not None:
			height += 1
			node = node.left
		if height <= 1:
			return height
		posl = 1
		posr = 2**(height-1)+1
		while posl < posr:
			mid = (posl + posr) / 2
			if self.dfs(root, mid, height):
				posl = mid+1
			else:
				posr = mid
		print posl
		return 2**(height-1)-1 + posl - 1