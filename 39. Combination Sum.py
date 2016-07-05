class Solution(object):
	def dfs(self, nb, rem, chose, ans, dp, candidates):
		# print nb, rem, chose
		if (nb, rem) in dp:
			if dp[(nb, rem)] == False:
				return False
		if nb == len(candidates):
			if rem == 0:
				ans.add(tuple(sorted(chose)))
				return True
			else:
				return False
		tag = False
		if candidates[nb] <= rem:
			chose.append(candidates[nb])
			tag = tag or self.dfs(nb+1, rem-candidates[nb], chose, ans, dp, candidates)
			chose.pop()
			chose.append(candidates[nb])
			tmp = self.dfs(nb, rem-candidates[nb], chose, ans, dp, candidates)
			chose.pop()
			tag = tag or tmp
		tmp = self.dfs(nb+1, rem, chose, ans, dp, candidates) # Attention, or is short!
		# print tmp
		tag = tag or tmp
		dp[(nb, rem)] = tag
		return tag

	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		dp = {}
		ans = set()
		self.dfs(0, target, [], ans, dp, candidates)
		ans = list(map(list,ans))
		print ans
		return ans

Solution().combinationSum([1,2,3], 10)