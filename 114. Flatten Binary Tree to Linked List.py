# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, order):
        if root is None:
            return
        order.append(root)
        if root.left is not None:
            self.dfs(root.left, order)
        if root.right is not None:
            self.dfs(root.right, order)
            
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        order = []
        self.dfs(root, order)
        if len(order) == 0:
            return
        for i in range(len(order)-1):
            order[i].right = order[i+1]
            order[i].left = None
        order[-1].right = None
        order[-1].left = None