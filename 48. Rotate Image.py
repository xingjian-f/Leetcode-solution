class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for k in range(len(matrix)/2):
        	for i in range(k, len(matrix)-k-1):
        		last_a = k
        		last_b = i 
        		last = matrix[last_a][last_b]
        		for j in range(4):
        			a = last_b
        			b = len(matrix)-last_a-1 
        			tmp = matrix[a][b]
        			# print last_a, last_b, last 
        			# print a, b, tmp
        			# print
        			matrix[a][b] = last 
        			last = tmp
        			last_a = a
        			last_b = b
        print matrix

Solution().rotate([[1,2],[3,4]])