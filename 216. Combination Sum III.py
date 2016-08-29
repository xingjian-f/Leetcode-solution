class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        from itertools import combinations
        ret = [] 
        for i in combinations(range(1, 10), k):
        	if sum(i) == n:
        		ret.append(list(i))
        return ret 

print Solution().combinationSum3(3, 9)