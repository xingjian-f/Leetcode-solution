class Solution(object):
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if len(s) == 0 or s[0]=='0':
			return 0
		if len(s) == 1:
			return 1
		dp = range(len(s))
		dp[0] = 1
		if s[1] == '0':
			dp[1] = 0
		else:
			dp[1] = 1
		if s[:2] <= '26':
			dp[1] += 1 
		for i in range(2, len(s)):
			if s[i] != '0':
				dp[i] = dp[i-1]
			else:
				dp[i] = 0
			if s[i-1:i+1] <= '26' and s[i-1] != '0':
				dp[i] += dp[i-2]
		return dp[len(s)-1]

print Solution().numDecodings('10')
# print '01' < '23'