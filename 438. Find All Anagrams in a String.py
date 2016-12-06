class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        cnt = Counter(p)
        if len(s) < len(p):
        	return []
        length = len(p)
        now = Counter(s[:length])
        ret = []
        for i in range(len(s)):
        	tag = True
        	for j in cnt:
        		if cnt[j] != now[j]:
        			tag = False
        			break
        	if tag is True:
        		ret.append(i)
        	if i+length < len(s):
        		now[s[i+length]] += 1
        		now[s[i]] -= 1
        	else:
        		break
        return ret 

print Solution().findAnagrams('ascba', 'abc')