class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        n = len(matrix)
        if n == 0:
        	return matrix
        m = len(matrix[0])
        for i in range(min(n/2, m/2)):
        	for j in range(i, m-i-1):
        		ret.append(matrix[i][j])
        	for j in range(i, n-i-1):
        		ret.append(matrix[j][m-i-1])
        	for j in reversed(range(i+1, m-i)):
        		ret.append(matrix[n-i-1][j])
        	for j in reversed(range(i+1, n-i)):
        		ret.append(matrix[j][i])

        if n<=m and n%2==1:
        	for j in range(n/2, m-n/2):
        		ret.append(matrix[n/2][j])
        if n>m and m%2==1:
        	for j in range(m/2, n-m/2):
        		ret.append(matrix[j][m/2])
        print ret 
        return ret

Solution().spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])