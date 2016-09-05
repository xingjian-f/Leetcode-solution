class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [nums[0]]
        for i in nums[1:]:
        	left.append(left[-1] * i)
        right = [nums[-1]]
        for i in nums[:-1][::-1]:
        	right.append(right[-1] * i)
        ret = [right[len(nums)-2]]
        for i in range(1, len(nums)-1):
        	ret.append(left[i-1] * right[len(nums)-i-2])
        ret.append(left[len(nums)-2])
       	return ret 

print Solution().productExceptSelf([1,2])