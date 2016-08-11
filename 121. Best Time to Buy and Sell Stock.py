class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
        	return 0
        left_min = range(len(prices))
        right_max = range(len(prices))
        left_min[0] = prices[0]
        for i in range(1, len(prices)):
        	left_min[i] = min(left_min[i-1], prices[i])
        right_max[-1] = -1e9
        for i in range(len(prices)-1)[::-1]:
        	right_max[i] = max(right_max[i+1], prices[i+1])
        ans = 0
        for i in range(len(prices)):
        	ans = max(right_max[i]-left_min[i], ans)
        return ans