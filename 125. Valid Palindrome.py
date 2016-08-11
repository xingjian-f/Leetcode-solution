class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_s = []
        for i in s:
        	if i.isalnum():
        		clean_s.append(i.lower())
       	s = ''.join(clean_s)
       	return s == s[::-1]


print Solution().isPalindrome("A man, a plan, a canal: Panama")