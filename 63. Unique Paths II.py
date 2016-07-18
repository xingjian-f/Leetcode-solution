class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        if n == 0:
        	return 0
        m = len(obstacleGrid[0])
        if m == 0:
        	return m
        dp = [[0 for i in range(m)] for j in range(n)]
        if obstacleGrid[0][0] == 1:
        	dp[0][0] = 0
        else:
        	dp[0][0] = 1
        for i in range(n):
        	for j in range(m):
        		if obstacleGrid[i][j] == 1:
        			continue
        		if i>0:
        			dp[i][j] += dp[i-1][j]
        		if j>0:
        			dp[i][j] += dp[i][j-1]
        return dp[n-1][m-1]