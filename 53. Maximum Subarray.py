class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1, len(nums)):
        	dp[i] = nums[i]
        	if dp[i-1]>0:
        		dp[i] += dp[i-1]
        	ans = max(ans, dp[i])
        return ans