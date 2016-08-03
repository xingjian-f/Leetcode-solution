# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, sum, seq, ans):
        import copy
        if root is None:
            return
        if root.val == sum and root.left is None and root.right is None:
            seq.append(root.val)
            print seq
            ans.append(copy.deepcopy(seq))
            seq.pop()
            return
        if root.left is not None:
            seq.append(root.val)
            self.dfs(root.left, sum-root.val, seq, ans)
            seq.pop()
        if root.right is not None:
            seq.append(root.val)
            self.dfs(root.right, sum-root.val, seq, ans)
            seq.pop()
        
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(root, sum, [], ans)
        return ans
        
"""
[]
1
[1]
1
[1,-1,2]
0
"""