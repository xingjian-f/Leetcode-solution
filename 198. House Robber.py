class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
        	return 0
        dp = [(0, 0), (nums[0], 0)]
        for i in nums[1:]:
        	chose = max(dp[-2][1], dp[-2][0]) + i 
        	not_chose = max(dp[-1][1], dp[-1][0])
        	dp.append((chose, not_chose))
        return max(dp[-1][0], dp[-1][1])

print Solution().rob([1,2,3,5])