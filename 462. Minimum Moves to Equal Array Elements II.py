class Solution(object):
	def step(self, pre_sums, nums, x):
		from bisect import bisect_left, bisect_right
		ret = 0
		left_pos = bisect_left(nums, x)
		if left_pos > 0:
			ret += x * (left_pos) - pre_sums[left_pos-1]
		right_pos = bisect_right(nums, x)
		if right_pos > 0 and right_pos < len(nums):
			ret += pre_sums[-1] - pre_sums[right_pos-1] - x * (len(nums)-right_pos)
		# print pre_sums, nums, x, ret
		return ret


	def minMoves2(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums = sorted(nums)
		pre_sums = [nums[0]]
		for i in nums[1:]:
			pre_sums.append(pre_sums[-1]+i)
		l, r = nums[0], nums[-1]+1
		ret = 1e9
		while l < r:
			mid = (l+r) / 2
			mid_val = self.step(pre_sums, nums, mid)
			ret = min(ret, mid_val)
			right_val = self.step(pre_sums, nums, mid+1)
			if mid_val == right_val:
				return mid_val
			elif mid_val < right_val:
				r = mid 
			else:
				l = mid+1
		return ret


print Solution().minMoves2([1,1,1,2,2,3])