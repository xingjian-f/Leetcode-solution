class Solution(object):
	def partition(self, nums):
		import random
		pivot = random.randint(0, len(nums)-1)
		left = 0
		nums[pivot], nums[-1] = nums[-1], nums[pivot]
		for i in xrange(len(nums)-1):
			if nums[i] >= nums[-1]:
				nums[i], nums[left] = nums[left], nums[i]
				left += 1
		left = min(len(nums)-1, left)
		nums[left], nums[-1] = nums[-1], nums[left]
		return left

		
	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		pivot = self.partition(nums)
		if k == pivot+1:
			return nums[k-1]
		elif k < pivot+1:
			return self.findKthLargest(nums[:pivot], k)
		else:
			return self.findKthLargest(nums[pivot+1:], k-pivot-1)


print Solution().findKthLargest([1, 4, 5, 5, 4, 1, 1], 5)