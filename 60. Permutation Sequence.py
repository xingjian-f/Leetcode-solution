class Solution(object):
	def dfs(self, rem, k):
		from math import factorial
		length = len(rem)
		tmp = factorial(length-1)
		if k > factorial(length) or length == 0:
			print 'bug'
			return
		elif length == 1:
			return str(rem[0])
		cnt = (k-1)/tmp
		next_k = k%tmp if k%tmp!=0 else tmp
		# print k, tmp, next_k
		next_rem = []
		for i in range(len(rem)):
			if i != cnt:
				next_rem.append(rem[i])
		# print rem, next_rem, next_k
		return str(rem[cnt]) + self.dfs(next_rem, next_k)


	def getPermutation(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: str
		"""
		print self.dfs(range(1, n+1), k) 
		return self.dfs(range(1, n+1), k)

Solution().getPermutation(4,6)