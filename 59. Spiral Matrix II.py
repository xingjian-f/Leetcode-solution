class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [range(n) for i in range(n)]
        if n == 0:
                return [] 
        m = n
        cnt = 1
        for i in range(n/2):
                for j in range(i, m-i-1):
                        matrix[i][j] = cnt
                        cnt += 1
                for j in range(i, n-i-1):
                        # print j, m-i-1
                        matrix[j][m-i-1] = cnt
                        cnt += 1
                for j in reversed(range(i+1, m-i)):
                        matrix[n-i-1][j] = cnt
                        cnt += 1
                for j in reversed(range(i+1, n-i)):
                        matrix[j][i] = cnt
                        cnt += 1
        if n%2==1:
                matrix[n/2][n/2] = cnt

        print matrix 
        return matrix

Solution().generateMatrix(3)