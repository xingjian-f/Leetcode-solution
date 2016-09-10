class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        dp = [1e9 for i in range(len(nums))]
        for num in nums:
        	posl = 0
        	posr = len(dp)
        	max_len = 1
        	while posl < posr:
        		mid = (posl + posr) / 2
        		if dp[mid] < num:
        			max_len = max(max_len, mid+1 + 1)
        			posl = mid+1
        		else:
        			posr = mid
        	dp[max_len-1] = min(dp[max_len-1], num)
        	ret = max(ret, max_len)
        # print dp
        return ret 

print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])