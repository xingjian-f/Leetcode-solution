class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        from copy import deepcopy
        board_2 = deepcopy(board)
        for i in range(len(board)):
        	for j in range(len(board[i])):
        		cnt = 0
        		cx = [-1,-1,-1,0,1,1,1,0]
        		cy = [-1,0,1,1,1,0,-1,-1]
        		for t in range(8):
        			tx = i + cx[t]
        			ty = j + cy[t]
        			if tx>=0 and tx<len(board) and ty>=0 and ty<len(board[i]) and board[tx][ty] == 1:
        				cnt += 1
        		if (board[i][j], cnt) in [(0, 3), (1, 2), (1, 3)]:
        			board_2[i][j] = 1
        		else:
        			board_2[i][j] = 0
        for i in range(len(board)):
        	for j in range(len(board[i])):
        		board[i][j] = board_2[i][j]

        print board

Solution().gameOfLife([[0, 1, 1, 1]])