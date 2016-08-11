class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
        	return 0
        dp = [1e9 for i in range(len(triangle))]
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
        	length = i+1
        	for j in range(1, length)[::-1]:
        		dp[j] = min(dp[j], dp[j-1])+triangle[i][j]
        	dp[0] += triangle[i][0]
        return min(dp)
   