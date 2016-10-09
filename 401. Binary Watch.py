class Solution(object):
	def parse(self, on):
		hours = 0
		for i in on:
			if i < 4:
				hours += 2**i
		minutes = 0
		for i in on:
			if i >= 4:
				minutes += 2**(i-4) 
		if hours > 11 or minutes > 59:
			return None
		return '%d:%02d' % (hours, minutes)


	def readBinaryWatch(self, num):
		"""
		:type num: int
		:rtype: List[str]
		"""
		from itertools import combinations
		ret = []
		for i in combinations(range(10), num):
			res = self.parse(i)
			if res is not None:
				ret.append(res)
		return ret

print Solution().readBinaryWatch(2)