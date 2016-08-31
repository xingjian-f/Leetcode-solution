class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		if len(nums) == 0:
			return []
		if len(nums) == 1:
			return [str(nums[0])]
		ret = []
		head = nums[0]
		last = nums[0]
		for i in range(1, len(nums)):
			val = nums[i]
			if val-last > 1:
				if last == head:
					ret.append(str(head))
				else:
					ret.append('%d->%d' % (head,last))
				head = val
			last = nums[i]
		if last == head:
			ret.append(str(head))
		else:
			ret.append('%d->%d' % (head,last))
		return ret 

print Solution().summaryRanges([1, 3])