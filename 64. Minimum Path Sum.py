class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n==0:
        	return 0
        m = len(grid[0])
        if m==0:
        	return 0
        dp = [[1e9 for i in range(m)] for j in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(n):
        	for j in range(m):
        		if i==0 and j==0:
        			continue
        		if i>0:
        			dp[i][j] = min(dp[i][j], dp[i-1][j]+grid[i][j])
        		if j>0:
        			dp[i][j] = min(dp[i][j], dp[i][j-1]+grid[i][j])
        return dp[n-1][m-1]