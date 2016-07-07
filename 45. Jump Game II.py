class Solution(object):
	def jump(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		pos = 0
		max_pos = nums[0]
		step = 0
		while True:
			if pos >= len(nums)-1:
				return step
			next_max_pos = max_pos
			for i in range(pos+1, min(max_pos+1, len(nums))):
				next_max_pos = max(next_max_pos, nums[i]+i)
			step += 1
			pos = max_pos
			max_pos = next_max_pos

Solution().jump([2,1])