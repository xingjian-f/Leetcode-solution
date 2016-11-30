class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ret = 0
        for i in range(len(board)):
        	for j in range(len(board[i])):
        		if board[i][j] == 'X':
        			if i>0 and board[i-1][j] == 'X':
        				continue
        			if j>0 and board[i][j-1] == 'X':
        				continue
        			ret += 1
        return ret

print Solution().countBattleships(["X",".","X"])