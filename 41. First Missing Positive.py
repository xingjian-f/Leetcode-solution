class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = len(nums)+1
        for i in range(len(nums)):
        	if nums[i] in ['used', 'has']:
        		continue
        	# print i, nums
        	if nums[i] <= len(nums) and nums[i] > 0:
        		pos = nums[i]-1
        		nums[i] = 'used'
        		# print pos
        		while True:
        			if nums[pos] in ['used', 'has'] or nums[pos] > len(nums) or nums[pos] <= 0:
        				nums[pos] = 'has'
        				break
        			else:
        				tmp = nums[pos]
        				nums[pos] = 'has'
        				pos = tmp-1
        # print nums
        for i in range(len(nums)):
        	if nums[i] != 'has':
        		ans = i+1
        		break
        print ans
        return ans
Solution().firstMissingPositive([2,1])