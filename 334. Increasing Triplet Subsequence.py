class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one = 1e10
        two = 1e10
        for i in nums:
        	# print one, two
        	if i > two:
        		return True
        	elif i < one:
        		one = i 
        	elif one < i and i < two:
        		two = i 
        return False

print Solution().increasingTriplet([1,2,1])