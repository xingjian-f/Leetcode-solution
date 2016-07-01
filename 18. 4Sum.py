class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)):
        	for j in range(i+1, len(nums)):
        		posl = j + 1
        		posr = len(nums) - 1
        		while posl < posr:
        			total = nums[i] + nums[j] + nums[posl] + nums[posr]
        			if total == target:
        				ans.add((nums[i], nums[j], nums[posl], nums[posr]))
        				posl += 1
        			elif total < target:
        				posl += 1
        			else:
        				posr -= 1
        ans = map(list, ans)
        print ans
        return ans

Solution().fourSum([0,0,0,0, -1, 1, -2, 1], 0) 