class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
        	return []
        nums = sorted(nums)
        dp = range(len(nums))
        head = 0
        max_len = 1
        for i in range(len(nums))[::-1]:
        	length = 0
        	tar = i
        	for j in range(i+1, len(nums)):
        		if nums[j]%nums[i] == 0:
        			if dp[j][0] > length:
        				length = dp[j][0]
        				tar = j
        	dp[i] = (length+1, tar)
        	if dp[i][0] > max_len:
        		max_len = dp[i][0]
        		head = i 
        ret = [nums[head]]
        # print dp
        while True:
        	if dp[head][1] != head:
        		head = dp[head][1]
        		ret.append(nums[head])
        	else:
        		break
        return ret

print Solution().largestDivisibleSubset([1,2,3,4,8,9,18,36])