class Solution(object):
	def canMeasureWater(self, x, y, z):
	    def gcd(x, y):
	            while x:
	                x, y = y % x, x
	            return y

	    return z == x+ y or (z < x + y and z % gcd(x, y) == 0)


print Solution().canMeasureWater(22003,31237,1)