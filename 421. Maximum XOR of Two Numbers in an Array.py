class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
        	for j in nums:
        		print bin(i)[2:], bin(j)[2:], i^j


print Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])