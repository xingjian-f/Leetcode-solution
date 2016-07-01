class Solution(object):
	def dfs(self, pos, nb_left, s, ans, n):
		if pos == 2*n:
			ans.append(''.join(s))
			return
		nb_right = pos-nb_left
		if nb_left < n:
			s.append('(')
			self.dfs(pos+1, nb_left+1, s, ans, n)
			s.pop()
		if nb_left > nb_right:
			s.append(')')
			self.dfs(pos+1, nb_left, s, ans, n)
			s.pop()

	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		ans = []
		s = []
		self.dfs(0, 0, s, ans, n)
		return ans

print Solution().generateParenthesis(4)