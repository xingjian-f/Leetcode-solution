class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0,0,1,2]
        for i in range(4, n+1):
        	tem = 0
        	for j in range(2, i-1):
        		tem = max(tem, max(j, dp[j]) * max(i-j, dp[i-j]))
        	dp.append(tem)
        return dp[n]

print Solution().integerBreak(10)