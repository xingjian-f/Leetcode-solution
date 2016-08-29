class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[::-1][k-1]

print Solution().findKthLargest([1,2,3], 3)