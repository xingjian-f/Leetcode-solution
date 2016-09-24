class Solution(object):
	def __init__(self):
		self.dp = {}


	def dfs(self, l, r):
		if (l, r) in self.dp:
			return self.dp[(l, r)]
		if l == r:
			return 0
		if r - l == 1:
			return l
		ret = 1e10
		for i in range(l+1, r):
			ret = min(ret, i + max(self.dfs(l, i-1), self.dfs(i+1, r)))
		self.dp[(l, r)] = ret
		return ret


	def getMoneyAmount(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		return self.dfs(1, n)

for i in range(1,100):
	print i, Solution().getMoneyAmount(i)