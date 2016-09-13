class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins)
        dp = [1e9 for i in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
        	for coin in coins:
        		if i >= coin:
        			dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[amount] >= 1e9:
        	return -1
        return dp[amount]

print Solution().coinChange([2, 3], 11000000)