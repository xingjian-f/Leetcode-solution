class Solution(object):
	
	def letterCombinations(self, digits):
		if len(digits) == 0:
			return []
		from itertools import product
		"""
		:type digits: str
		:rtype: List[str]
		"""
		trans = [' ', '*', 'abc', 'def','ghi','jkl','mno','pqrs','tuv','wxyz']
		ans = []
		for digit in digits:
			digit = int(digit)
			ans.append(trans[digit])
		ans = map(lambda x: ''.join(x), list(product(*ans)))
		print ans
		return ans
		
Solution().letterCombinations('')