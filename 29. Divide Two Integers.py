class Solution(object):
	def divide(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		ans = 0
		tag = (divisor<0 and dividend>0) or (divisor>0 and dividend<0) 
		divisor = abs(divisor)
		dividend = abs(dividend)
		rem = dividend
		divs = [divisor]
		muls = [1]
		if divisor == 0:
			return -1
		cnt = 0
		while rem >= divs[0]:
			if rem >= divs[cnt]:
				rem -= divs[cnt]
				ans += muls[cnt]
				divs.append(divs[cnt]+divs[cnt])
				muls.append(muls[cnt]+muls[cnt])
				cnt += 1
			else:
				cnt -= 1
		if tag:
			ans = -ans
		ans = min(2147483647, ans)
		return ans