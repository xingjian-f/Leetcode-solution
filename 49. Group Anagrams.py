class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for i in strs:
        	tmp = tuple(sorted(i))
        	if tmp in ans:
        		ans[tmp].append(i)
        	else:
        		ans[tmp] = [i]
        print ans.values()
        return ans.values()