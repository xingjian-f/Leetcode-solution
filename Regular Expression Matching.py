class Solution(object):
	def cal(self, i, j, s, p, dp):
		if dp[i][j] != -1:
			return dp[i][j]
		if i>=len(s) and j>=len(p):
			return True
		if j+1 < len(p) and p[j+1] == '*':
			dp[i][j] = self.cal(i,j+2,s,p,dp)
			if i<len(s) and j<len(p):
				dp[i][j] = dp[i][j] or (p[j] in ['.', s[i]] and (self.cal(i+1,j+2,s,p,dp) or self.cal(i+1,j,s,p,dp)))
		elif i<len(s) and j<len(p):
			dp[i][j] = p[j] in ['.', s[i]] and self.cal(i+1,j+1,s,p,dp)
		else:
			dp[i][j] = False
		return dp[i][j]

	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		maxn = max(len(s), len(p)) + 5
		dp = [[-1 for i in range(maxn)] for j in range(maxn)]	
 
		return self.cal(0,0,s,p,dp)