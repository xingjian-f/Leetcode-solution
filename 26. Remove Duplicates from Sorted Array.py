class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)-1
        pos = 1
        while length > 0:
        	if nums[pos] == nums[pos-1]:
        		# for j in range(pos, length-1):
        		# 	nums[j] = nums[j+1]	
        		del nums[pos]
        	else:
        		pos += 1
        	length -= 1
       	return len(nums)