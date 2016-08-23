class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = []
        for i in nums:
        	if len(s) == 0 or i == s[-1]:
        		s.append(i)
        	else:
        		s.pop()
        return s[0]