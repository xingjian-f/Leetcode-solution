class Solution(object):
	def combine(self, nums, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		from itertools import combinations
		return map(list, list(combinations(nums, k)))

	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		res = []
		for i in range(len(nums)+1):
			res.extend(self.combine(nums, i))
		return res

print Solution().subsets([2,3,6])
