class Solution(object):
	def find_fa(self, x, fa):
		# print x
		if fa[x] == x:
			return x
		fa[x] = self.find_fa(fa[x], fa)
		return fa[x]


	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
			return 0
		nums = set(nums)
		fa = {}
		size = {}
		for i in nums:
			fa[i] = i 
			size[i] = 1
		for i in nums:
			if i-1 in nums:
				fa_x = self.find_fa(i, fa)
				fa_y = self.find_fa(i-1, fa)
				if fa_x != fa_y:
					fa[fa_x] = fa_y
					size[fa_y] += size[fa_x]
			if i+1 in nums:
				fa_x = self.find_fa(i, fa)
				fa_y = self.find_fa(i+1, fa)
				if fa_x != fa_y:
					fa[fa_y] = fa_x
					size[fa_x] += size[fa_y]
		# print fa 
		# print size
		return max([size[i] for i in size])


# print Solution().longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])