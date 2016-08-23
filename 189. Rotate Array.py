class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        from copy import deepcopy
        a = deepcopy(nums)
        for i in range(len(nums)):
        	nums[(i+k)%len(nums)] = a[i]