class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = 0
        for i in nums:
        	if i != val:
        		nums[pos] = i 
        		pos += 1
        return pos