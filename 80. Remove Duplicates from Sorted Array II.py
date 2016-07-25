class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)-1
        if length<=0:
        	return 0
        pos = 1
        cnt = 1
        last = nums[0]
        while length > 0:
        	if nums[pos] == last:
        		if cnt >= 2:
        			del nums[pos]
        		else:
        			pos += 1
        			cnt += 1
        	else:
        		last = nums[pos]
        		pos += 1
        		cnt = 1
        	length -= 1
       	return len(nums)

print Solution().removeDuplicates([1,1,1,1,1,2,3,3,4,4,5])