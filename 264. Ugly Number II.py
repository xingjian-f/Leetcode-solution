class Solution(object):
	def __init__(self):
		self.ugly = set([1])
		max_int = 2 ** 32
		for i in range(32):
			for j in range(32):
				if 2 ** i * 3 ** j > max_int:
					break
				for k in range(32):
					tem = 2**i * 3**j * 5**k
					if tem > max_int:
						break
					self.ugly.add(tem)
		self.ugly = sorted(self.ugly)


	def nthUglyNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		print self.ugly, len(self.ugly)
		return self.ugly[n-1]

print Solution().nthUglyNumber(1000)