class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        front = [(matrix[0][0], 0, 0)]
        for _ in range(k-1):
        	top = heapq.heappop(front)
        	x, y = top[1], top[2]
        	# print x, y
        	if x < len(matrix)-1:
        		heapq.heappush(front, (matrix[x+1][y], x+1, y))
        		matrix[x+1][y] = 1e9
        	if y < len(matrix[0])-1:
        		heapq.heappush(front, (matrix[x][y+1], x, y+1))
        		matrix[x][y+1] = 1e9
        # print front
        return heapq.heappop(front)[0]

print Solution().kthSmallest([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 9)