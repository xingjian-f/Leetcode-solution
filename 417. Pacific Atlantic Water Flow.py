class Solution(object):
	def bfs(self, vis, queue, matrix):
		from collections import deque
		queue = deque(queue)
		cx = [-1,0,1,0]
		cy = [0,1,0,-1]
		# print queue
		while len(queue) > 0:
			x, y = queue.popleft()
			# print x, y
			if vis[x][y] == 1:
				continue
			vis[x][y] = 1
			for i in range(4):
				tx = x + cx[i]
				ty = y + cy[i]
				if (tx>=0 and tx<len(matrix) and ty>=0 and ty<len(matrix[0]) 
					and vis[tx][ty]==0 and matrix[x][y]<=matrix[tx][ty]):
					queue.append((tx, ty))


	def pacificAtlantic(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[List[int]]
		"""
		if len(matrix) == 0:
			return []
		
		up = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
		queue = []
		for i in range(len(matrix[0])):
			queue.append((0, i))
		self.bfs(up, queue, matrix)

		left = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
		queue = []
		for i in range(len(matrix)):
			queue.append((i, 0))
		self.bfs(left, queue, matrix)

		down = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
		queue = []
		for i in range(len(matrix[0])):
			queue.append((len(matrix)-1, i))
		self.bfs(down, queue, matrix)

		right = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
		queue = []
		for i in range(len(matrix)):
			queue.append((i, len(matrix[0])-1))
		self.bfs(right, queue, matrix)

		ret = []
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				if (up[i][j]==1 or left[i][j]==1) and (down[i][j]==1 or right[i][j]==1):
					ret.append([i, j])
		return ret


print Solution().pacificAtlantic([[1,2],[2,1]])