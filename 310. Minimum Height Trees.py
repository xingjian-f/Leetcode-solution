class Solution(object):
	def bfs(self, s, edges, n):
		from collections import deque
		queue = deque([(s, 1)])
		vis = [0 for i in range(n)]
		vis[s] = 1
		ret1, ret2 = None, None
		while len(queue) > 0:
			pos, step = queue.popleft()
			# print pos, step
			ret1, ret2 = pos, step
			if pos in edges:
				for nei in edges[pos]:
					if vis[nei] == 0:
						queue.append((nei, step+1))
						vis[nei] = 1
		return (ret1, ret2)


	def bfs2(self, s, edges, n, to_go):
		from collections import deque
		queue = deque([(s, 1)])
		vis = [0 for i in range(n)]
		while len(queue) > 0:
			pos, step = queue.popleft()
			if step == to_go:
				return pos
			if pos in edges:
				for nei in edges[pos]:
					if vis[nei] == 0:
						queue.append((nei, step+1))
						vis[nei] = 1


	def findMinHeightTrees(self, n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		g = {}
		for i in edges:
			x, y = i[0], i[1] 
			if x not in g:
				g[x] = [y]
			else:
				g[x].append(y)
			if y not in g:
				g[y] = [x]
			else:
				g[y].append(x)
		end = self.bfs(0, g, n)[0]
		length = self.bfs(end, g, n)[1]
		# print length
		if length % 2 == 1:
			return [self.bfs2(end, g, n, length/2+1)]
		else:
			return [self.bfs2(end, g, n, length/2), self.bfs2(end, g, n, length/2+1)]

print Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
print Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
print Solution().findMinHeightTrees(3, [[0, 1], [0, 2]])