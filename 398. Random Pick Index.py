class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.numsSize = len(nums)
        self.nums = nums


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        ret = -1
        cnt = 1
        for i in range(self.numsSize):
            if self.nums[i] == target:
                if random.random() <= 1.0/cnt:
                    ret = i 
                cnt += 1
        return ret 


# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3,4,4,1])
param_1 = obj.pick(4)
print param_1

from collections import Counter
