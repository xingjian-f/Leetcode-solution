class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
        	if nums[i] != 0:
        		if i != pos:
        			nums[pos], nums[i] = nums[i], nums[pos]
        		pos += 1