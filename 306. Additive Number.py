class Solution(object):
	def dfs(self, last1, last2, pos, num):
		print last1, last2, pos, num
		if pos >= len(num):
				return False
		ret = False
		if last1 is None:	
			if num[pos] == '0':
				return self.dfs(0, None, pos+1, num)
			else:
				for i in range(pos, len(num)):
					ret = ret or self.dfs(int(num[pos:i+1]), None, i+1, num)
		elif last2 is None:
			if num[pos] == '0':
				return self.dfs(last1, 0, pos+1, num)
			else:
				for i in range(pos, len(num)):
					ret = ret or self.dfs(last1, int(num[pos:i+1]), i+1, num)
		else:
			if num[pos] == '0':
				if last1 + last2 == 0:
					if pos+1 == len(num):
						return True
					return self.dfs(last2, 0, pos+1, num)
				else:
					return False
			else:
				for i in range(pos, len(num)):
					if last1 + last2 == int(num[pos:i+1]):
						if i+1 == len(num):
							return True
						ret = ret or self.dfs(last2, last1+last2, i+1, num)

		return ret


	def isAdditiveNumber(self, num):
		"""
		:type num: str
		:rtype: bool
		"""
		return self.dfs(None, None, 0, num)


print Solution().isAdditiveNumber('123123246')