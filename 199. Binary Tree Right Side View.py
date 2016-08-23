# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        level_order = []
        from collections import deque
        queue = deque()
        if root is not None:
        	queue.append((root, 1))
        last_level = 0
        while len(queue) > 0:
        	node, level = queue.popleft()
        	if level > last_level:
        		level_order.append([node.val])
        		last_level = level 
        	else:
        		level_order[-1].append(node.val)
        	if node.left is not None:
        		queue.append((node.left, level+1))
        	if node.right is not None:
        		queue.append((node.right, level+1))
        return [i[-1] for i in level_order]