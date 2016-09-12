class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.dp = [range(len(matrix[0])) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.dp[i][j] = matrix[i][j]
                if i > 0:
                    self.dp[i][j] += self.dp[i-1][j]
                if j > 0:
                    self.dp[i][j] += self.dp[i][j-1]
                if i>0 and j>0:
                    self.dp[i][j] -= self.dp[i-1][j-1]



    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret = self.dp[row2][col2]
        if row1>0:
            ret -= self.dp[row1-1][col2]
        if col1>0:
            ret -= self.dp[row2][col1-1]
        if row1>0 and col1>0:
            ret += self.dp[row1-1][col1-1]
        return ret


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix([  [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]])
numMatrix = NumMatrix([[-2]])
print numMatrix.sumRegion(0,0,0,0)
# print numMatrix.sumRegion(0, 1, 2, 3)
# print numMatrix.sumRegion(1, 2, 3, 4)
# print numMatrix.sumRegion(2, 1, 4, 3) #-> 8
# print numMatrix.sumRegion(1, 1, 2, 2) #-> 11
# print numMatrix.sumRegion(1, 2, 2, 4) #-> 12