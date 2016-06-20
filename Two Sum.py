class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = {}
        for i, num in enumerate(nums):
        	if num in record:
        		record[num].append(i)
        	else:
				record[num] = [i]
        for i, num in enumerate(nums):
        	der = target-num
        	if der in record:
        		if der == num:
        			if len(record[der]) > 1:
        				return [i, record[der][-1]]
        		else:
        			return [i, record[der][0]]

a = Solution()
print a.twoSum([-1,-1],-2)
print a.twoSum([2, 7, 11, 15], 18)