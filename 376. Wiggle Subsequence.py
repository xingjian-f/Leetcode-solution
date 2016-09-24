class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
        	return 0
        ret = 1
        tag = 1
        for i in range(1, len(nums)):
        	if tag == 1 and nums[i] > nums[i-1]:
    			ret += 1
    			tag = 0
        	if tag == 0 and nums[i] < nums[i-1]:
    			ret += 1
    			tag = 1
    	tem = ret
    	ret = 1
        tag = 0
        for i in range(1, len(nums)):
        	if tag == 1 and nums[i] > nums[i-1]:
    			ret += 1
    			tag = 0
        	if tag == 0 and nums[i] < nums[i-1]:
    			ret += 1
    			tag = 1
        return max(tem, ret)

print Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9])