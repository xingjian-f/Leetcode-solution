class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(n):
        	for j in range(m):
        		if matrix[i][j] == 0:
        			rows.add(i)
        			cols.add(j)
        for i in rows:
        	for j in range(m):
        		matrix[i][j] = 0
        for i in cols:
        	for j in range(n):
        		matrix[j][i] = 0