class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		pos = 0
		max_pos = nums[0]
		while True:
			if max_pos >= len(nums)-1:
				return True
			next_max_pos = max_pos
			for i in range(pos+1, min(max_pos+1, len(nums))):
				next_max_pos = max(next_max_pos, nums[i]+i)
			pos = max_pos
			if next_max_pos == max_pos:
				return False
			max_pos = next_max_pos