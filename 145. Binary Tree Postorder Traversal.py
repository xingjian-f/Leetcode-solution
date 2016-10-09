# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root is not None:
        	if root.left is not None:
        		ret.extend(self.postorderTraversal(root.left))
        	if root.right is not None:
        		ret.extend(self.postorderTraversal(root.right))
        	ret.append(root.val)
        return ret 