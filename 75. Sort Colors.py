class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = [0 for i in range(3)]
        for i in nums:
        	cnt[i] += 1
        pos = 0
        for idx, i in enumerate(cnt):
        	for j in range(i):
        		nums[pos+j] = idx
        	pos += i 
        print nums