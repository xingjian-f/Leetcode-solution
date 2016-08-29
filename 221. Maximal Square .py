class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        up = [range(len(matrix[i])) for i in range(len(matrix))]
        left = [range(len(matrix[i])) for i in range(len(matrix))]
        for i in range(len(matrix)):
        	for j in range(len(matrix[i])):
        		if matrix[i][j] == '0':
        			up[i][j] = 0
        			left[i][j] = 0
        		else:
        			up[i][j] = 1
        			left[i][j] = 1
        			if i > 0:
        				up[i][j] += up[i-1][j]
        			if j > 0:
        				left[i][j] += left[i][j-1]

        dp = [range(len(matrix[i])) for i in range(len(matrix))]
        ans = 0
        for i in range(len(matrix)):
        	for j in range(len(matrix[i])):
        		if matrix[i][j] == '0':
        			dp[i][j] = 0
        		else:
        			dp[i][j] = 1
        			if i > 0 and j > 0:
        				max_width = min(dp[i-1][j-1]+1, left[i][j])
        				max_height = min(dp[i-1][j-1]+1, up[i][j])
        				dp[i][j] = min(max_height, max_width)
        			ans = max(ans, dp[i][j]**2)

        # print matrix
        # print up
        # print left
        # print dp
        return ans

print Solution().maximalSquare(["10100","10111","11111","10010"])