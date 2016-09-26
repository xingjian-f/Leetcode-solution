class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        c = Counter(list(ransomNote))
        b = Counter(list(magazine))
        for i in c:
        	if i in b and b[i] >= c[i]:
        		continue
        	else:
        		return False
        return True

print Solution().canConstruct('c', 'aab')