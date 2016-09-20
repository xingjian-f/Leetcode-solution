class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_s = []
        for i in s:
        	if i in vowels:
        		vowels_s.append(i)

        vowels_s = vowels_s[::-1]
        ret = []
        cnt = 0
        for i in range(len(s)):
        	if s[i] in vowels:
        		ret.append(vowels_s[cnt])
        		cnt += 1
        	else:
        		ret.append(s[i])
        return ''.join(ret)

print Solution().reverseVowels('leetcode')