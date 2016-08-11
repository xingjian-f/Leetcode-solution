class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
        	return [[]]
        ans = []
        if s == s[::-1]:
        	ans.append([s])
        for i in range(1,len(s)):
        	# print s[i:], s[i:][::-1], i, len(s[i:])
        	if s[i:] == s[i:][::-1]:
        		left = self.partition(s[:i])
        		# print left
        		if len(left) > 0:
        			for j in left:
        				j.append(s[i:])
        				ans.append(j)
        # print 'ans', ans
        return ans

print Solution().partition('asas')