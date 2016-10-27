class Solution(object):
	def dfs(self, x, y, matrix, dp):
		if (x, y) in dp:
			return dp[(x, y)]
		ret = 0
		cx = [-1,0,1,0]
		cy = [0,1,0,-1]
		for i in range(4):
			tx = x + cx[i]
			ty = y + cy[i]
			if (tx>=0 and tx<len(matrix) and ty>=0 and 
				ty<len(matrix[0]) and matrix[tx][ty]>matrix[x][y]):
				ret = max(ret, self.dfs(tx, ty, matrix, dp))
		dp[(x, y)] = ret + 1
		return ret + 1


	def longestIncreasingPath(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: int
		"""
		ret = 0
		dp = {}
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				ret = max(ret, self.dfs(i, j, matrix, dp))
		# print dp
		return ret 

print Solution().longestIncreasingPath([[1,2,1,4]])