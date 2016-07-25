class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        from itertools import combinations
        return map(list, list(combinations(range(1,n+1), k)))
print Solution().combine(4,2)