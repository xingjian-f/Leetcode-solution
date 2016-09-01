class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rec = {}
        for i in nums:
        	rec[i] = rec.get(i, 0) + 1
        ret = []
        for i in rec:
        	if rec[i] > len(nums)/3:
        		ret.append(i)
        return ret