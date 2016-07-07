class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        a = permutations(nums)
        return map(list,list(a))


Solution().permute([1,2,3])