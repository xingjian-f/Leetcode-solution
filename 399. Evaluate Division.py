class Solution(object):
	def calcEquation(self, equations, values, queries):
		"""
		:type equations: List[List[str]]
		:type values: List[float]
		:type queries: List[List[str]]
		:rtype: List[float]
		"""
		node_id = {}
		cnt = 0
		for i in equations:
			for j in i:
				if j not in node_id:
					node_id[j] = cnt
					cnt += 1

		n = len(node_id)
		dist = [[None for i in range(n)] for _ in range(n)]
		for idx, i in enumerate(equations):
			ida = node_id[i[0]]
			idb = node_id[i[1]]
			dist[ida][idb] = values[idx]
			dist[idb][ida] = 1 / values[idx]
			dist[ida][ida] = 1.0
			dist[idb][idb] = 1.0

		for k in range(n):
			for i in range(n):
				for j in range(n):
					if dist[i][j] is not None or dist[i][k] is None or dist[k][j] is None:
						continue
					dist[i][j] = dist[i][k] * dist[k][j]

		# print dist
		ret = []
		for i in queries:
			if i[0] not in node_id or i[1] not in node_id:
				ret.append(-1.0)
			else:
				x = node_id[i[0]]
				y = node_id[i[1]]
				ret.append(dist[x][y] if dist[x][y] is not None else -1.0)
		return ret


# print Solution().calcEquation([ ["a","b"],["b","c"] ]
# ,[2.0,3.0],
# [ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ])
# print Solution().calcEquation([['a', 'a'], ['b', 'b']], [1.0, 2.3], [['b','a'] ])