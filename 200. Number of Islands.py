class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        vis = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        ans = 0
        from collections import deque
        queue = deque()
        for i in range(len(grid)):
        	for j in range(len(grid[0])):
        		if grid[i][j] == '1' and vis[i][j] == 0:
        			ans += 1
        			vis[i][j] = 1
        			queue.append((i, j))
        			while len(queue) > 0:
        				x, y = queue.popleft()
        				cx = [-1, 0, 1, 0]
        				cy = [0, 1, 0, -1]
        				for t in range(4):
        					tx = x + cx[t]
        					ty = y + cy[t]
        					if tx>=0 and tx < len(grid) and ty>=0 and ty < len(grid[0]) and grid[tx][ty] == '1' and vis[tx][ty] == 0:
        						queue.append((tx, ty))
        						vis[tx][ty] = 1
        return ans