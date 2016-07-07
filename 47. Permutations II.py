class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        return map(list,set(permutations(nums)))
print Solution().permuteUnique([1,1,2,3])