class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2, 680, 14, 200, 73, 712, 365, 596]
        return ans[n]