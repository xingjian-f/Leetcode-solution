class Solution(object):
	def countNumbersWithUniqueDigits(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		ret = 1
		
		for length in range(1, n+1):
			tag = True
			tem = 1
			choice = 9
			for i in range(length):
				tem *= choice
				if tag:
					tag = False
				else:
					choice -= 1
			ret += tem
		return ret

print Solution().countNumbersWithUniqueDigits(12)