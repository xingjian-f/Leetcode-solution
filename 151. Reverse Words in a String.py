class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')[::-1]
        ret = []
        for i in s:
        	if len(i) > 0:
        		ret.append(i) 
        ret = ' '.join(ret)
        return ret

print Solution().reverseWords(' ')