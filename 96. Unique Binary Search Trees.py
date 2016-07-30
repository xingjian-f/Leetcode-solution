class Solution(object):
	def __init__(self):
		self.dp = {}

	def numTrees(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n in self.dp:
			return self.dp[n]
		ret = 0
		if n == 0:
			return 1
		for i in range(1, n+1):
			ret += self.numTrees(i-1) * self.numTrees(n-i)
		self.dp[n] = ret 
		return ret

print Solution().numTrees(3)