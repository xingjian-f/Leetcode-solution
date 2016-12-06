class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        dp = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
        	for j in range(len(matrix[i])):
        		dp[i][j] = matrix[i][j]
        		if i>0:
        			dp[i][j] += dp[i-1][j]
        		if j>0:
        			dp[i][j] += dp[i][j-1]
        		if i>0 and j>0:
        			dp[i][j] -= dp[i-1][j-1]

        ret = -1e9
        for i in range(len(matrix)):
        	for j in range(len(matrix[i])):
        		for u in range(i, len(matrix)):
        			for v in range(j, len(matrix[i])):
        				val = dp[u][v]
        				if i>0:
        					val -= dp[i-1][v]
        				if j>0:
        					val -= dp[u][j-1]
        				if i>0 and j>0:
        					val += dp[i-1][j-1]
        				if val <= k:
        					ret = max(val, ret)

        return ret


print Solution().maxSumSubmatrix([[1],[2]], 2)