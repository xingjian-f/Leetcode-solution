class Solution(object):
	def dfs(self, pos, tar, nums, dp):
		if (pos, tar) in dp:
			return dp[(pos, tar)]
		if pos == len(nums):
			return False
		if tar == nums[pos]:
			ret = True
		elif tar < nums[pos]:
			ret = False
		else:
			ret = self.dfs(pos+1, tar, nums, dp) or self.dfs(pos+1, tar-nums[pos], nums, dp)
		dp[(pos, tar)] = ret 
		return ret 


	def canPartition(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		nums = sorted(nums)
		total = sum(nums)
		if total % 2 == 0:
			dp = {}
			return self.dfs(0, total/2, nums, dp)
		else:
			return False


# print Solution().canPartition([39,68,6,73,8,81,90,12,60,87,20,84,83,8,55,62,97,8,77,51,71,96,3,29,90,63,2,14,38,60,33,34,79,41,83,32,17,67,63,97,23,16,19,8,95,57,56,96,31,85,47,19,86,60,68,11,84,5,70,87,70,49,30,86,63,90,73,70,86,49,98,91,57,48,98,35,22,23,78,40,96,82,94,14,78,49,43,12,53,23,22,90,87,92,1,39,24,7,54,84])