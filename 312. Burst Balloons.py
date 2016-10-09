class Solution(object):
	def dfs(self, l, r, left_val, right_val, nums, dp):
		if (l, r, left_val, right_val) in dp:
			return dp[(l, r, left_val, right_val)]
		if l > r:
			return 0
		if l == r:
			return nums[l] * left_val * right_val
		ret = 0
		for i in range(l, r+1):
			ret = max(ret, nums[i]*left_val*right_val + 
				self.dfs(l, i-1, left_val, nums[i], nums, dp) + 
				self.dfs(i+1, r, nums[i], right_val, nums, dp))
		# print l, r, left_val, right_val, 'xxx', ret
		dp[(l, r, left_val, right_val)] = ret
		return ret 


	def maxCoins(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		dp = {}
		return self.dfs(0, len(nums)-1, 1, 1, nums, dp)
		# print dp
		# return dp[(0, len(nums)-1, 1, 1)]


print Solution().maxCoins([4,1,4,9,4,1,8,1,8,6,9,1,2,0,9,6,4,1,7,9,5,4,4,0]) # 5872
print Solution().maxCoins([])