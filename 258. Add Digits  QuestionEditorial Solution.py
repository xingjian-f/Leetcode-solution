class Solution(object):
	def addDigits(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		while num >= 10:
			new_num = 0
			while num > 0:
				new_num += num%10
				num /= 10
			num = new_num
		return num

print Solution().addDigits(19)