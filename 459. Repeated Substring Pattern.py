class Solution(object):
	def check(self, s, length):
		pos = 0
		while pos+2*length <= len(s):
			if s[pos:pos+length] != s[pos+length:pos+2*length]:
				return False
			pos += length
		# print s, length
		return True


	def repeatedSubstringPattern(self, strs):
		"""
		:type str: str
		:rtype: bool
		"""
		length = len(strs)
		for i in range(1, length):
			if length%i == 0 and self.check(strs, i):
				return True
		return False


print Solution().repeatedSubstringPattern('12211221')