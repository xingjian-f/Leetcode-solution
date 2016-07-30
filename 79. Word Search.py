class Solution(object):
	def dfs(self, board, word, posx, posy):
		if word == '':
			return True
		ret = False
		cx = [0,-1,0,1]
		cy = [-1,0,1,0]
		for i in range(4):
			tx = posx+cx[i]
			ty = posy+cy[i]
			if tx>=0 and tx<len(board) and ty>=0 and ty<len(board[0]) and board[tx][ty] == word[0]:
				board[tx][ty] = -1
				ret = ret or self.dfs(board, word[1:], tx, ty)
				board[tx][ty] = word[0]
		return ret


	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		if word == '':
			return True
		ret = False
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == word[0]:
					board[i][j] = -1
					ret = ret or self.dfs(board, word[1:], i, j)
					board[i][j] = word[0]
		return ret