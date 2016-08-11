class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
        	return
        n = len(board)
        m = len(board[0])
        vis = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        
        for i in range(len(board)):
        	for j in range(len(board[i])):
        		if vis[i][j] == 1 or board[i][j] == 'X':
        			continue
        		else:
        			tag = 0
        			queue = [(i,j)]
        			vis[i][j] = 1
        			pos = 0
        			print i, j, 'a'
        			while pos < len(queue):
        				x, y = queue[pos]
        				pos += 1
        				print x, y
        				if x in [0, n-1] or y in [0, m-1]:
        					tag = 1
        				cx = [-1,0,1,0]
        				cy = [0,1,0,-1]
        				for k in range(4):
        					tx = x+cx[k]
        					ty = y+cy[k]
        					if tx >= 0 and tx < n and ty >= 0 and ty < m and vis[tx][ty] == 0 and board[tx][ty] == 'O':
        						queue.append((tx, ty))
        						vis[tx][ty] = 1
        			if tag == 0:
        				for k in queue:
        					x, y = k 
        					board[x][y] = 'X'

       	for i in board:
       		print i


Solution().solve([['X','X', 'X', 'X'],[
'X', 'O', 'O', 'X'],[
'X', 'X', 'O', 'X'],[
'X', 'O', 'X', 'X']])