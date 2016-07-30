class Solution(object):
	def combine(self, nums, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		from itertools import combinations
		return map(list, list(combinations(nums, k)))

	def subsetsWithDup(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		res = set()
		for i in range(len(nums)+1):
			for i in self.combine(nums, i):
				res.add(tuple(sorted(i)))
		res = list(map(list, res))
		# print res
		return res
Solution().subsetsWithDup([1,2,2,3])