class Solution(object):
	def __init__(self):
		self.dp = {}


	def combinationSum4(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if target in self.dp:
			return self.dp[target]
		if target == 0:
			return 1
		ret = 0
		for i in nums:
			if i <= target:
				ret += self.combinationSum4(nums, target-i)
		self.dp[target] = ret
		return ret 

print Solution().combinationSum4([1,2,3],2)