class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
        	return 0
        dp = range(len(prices))
        max_profit = 1e-9
        for i in range(len(prices)):
        	if i == 0:
        		dp[0] = (0, 0)
        		max_profit = -prices[0]
        	else:
        		not_sold = max(dp[i-1][0], dp[i-1][1])
        		sold = prices[i] + max_profit
        		dp[i] = (sold, not_sold)
        		if i > 1:
        			max_profit = max(max_profit, -prices[i] + max(dp[i-1][1], dp[i-2][0]))
        		else:
        			max_profit = max(max_profit, -prices[i])

        return max(dp[-1][0], dp[-1][1])

print Solution().maxProfit([1,2,4])