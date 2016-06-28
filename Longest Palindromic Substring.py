class Solution(object):
	def longestPalindrome(self, s):
		length = len(s)
		maxl = 1
		posl = 0
		posr = 0
		for i in range(1, length):
			if i-maxl-1>=0 and s[i-maxl-1:i+1]==s[i-maxl-1:i+1][::-1]:
				maxl += 2
				posl = i-maxl+1
				posr = i 
			elif i-maxl>=0 and s[i-maxl:i+1]==s[i-maxl:i+1][::-1]:
				maxl += 1
				posl = i-maxl+1 
				posr = i  
		return s[posl:posr+1]

print Solution().longestPalindrome('121')
s = '123'
print s[2::-1]