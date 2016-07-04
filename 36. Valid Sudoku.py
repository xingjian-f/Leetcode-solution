class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isvalid(x):
        	cnt = {}
        	for i in x:
        		cnt[i] = cnt.get(i, 0) + 1
        	for i in cnt:
        		if i != '.' and cnt[i]>1:
        			return False
        	return True

       	ret = True
       	for i in board:
       		ret = ret and isvalid(i)
       	for i in range(len(board)):
       		x = [board[j][i] for j in range(len(board))]
       		ret = ret and isvalid(x)
       	posxs = [0,0,0,3,3,3,6,6,6]
       	posys = [0,3,6,0,3,6,0,3,6]
       	for posx in posxs:
       		for posy in posys:
       			x = []
       			for i in range(3):
       				for j in range(3):
       					x.append(board[i+posx][j+posy])
       			ret = ret and isvalid(x)
       	return ret