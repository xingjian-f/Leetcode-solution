class Solution(object):	
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		nums = sorted(nums)
		min_der = 1e9
		ans = 1e9
		for i in range(len(nums)):
			posl = i+1
			posr = len(nums)-1
			while posl < posr:
				total = nums[i] + nums[posl] + nums[posr]
				der = abs(total -target)
				if der < min_der:
					min_der = der
					ans = total 
				if total == target:
					break
				elif total < target:
					posl += 1
				else:
					posr -= 1
		print ans
		return ans