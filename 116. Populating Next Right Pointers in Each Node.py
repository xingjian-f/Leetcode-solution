# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        level_order = []
        from collections import deque
        queue = deque()
        if root is not None:
        	queue.append(root)
        while len(queue) > 0:
        	top = queue.popleft()
        	level_order.append(top)
        	if top.left is not None:
        		queue.append(top.left)
        	if top.right is not None:
        		queue.append(top.right)
        cnt = 1
        level = 1
        for i in range(len(level_order)):
        	node = level_order[i]
        	cnt -= 1
        	if cnt == 0:
        		node.next = None
        		level *= 2
        		cnt = level 
        	else:
        		node.next = level_order[i+1]