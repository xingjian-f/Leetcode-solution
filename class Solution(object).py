class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		stack = []
		valid = True
		left = ['(', '[', '{']
		right = [')', ']', '}']
		for i in s:
			if i in left:
				stack.append(i)	
			elif i in right:
				if len(stack) == 0:
					valid = False
					break
				val = stack.pop()
				if left.index(val) != right.index(i):
					valid = False
					break
		if len(stack) > 0:
			valid = False
		return valid