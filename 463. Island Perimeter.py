class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        for i in range(len(grid)):
        	for j in range(len(grid[i])):
        		if grid[i][j] == 1:
        			if i == 0:
        				ret += 1
        			elif grid[i-1][j] == 0:
        				ret += 1
        			if i == len(grid)-1:
        				ret += 1
        			elif grid[i+1][j] == 0:
        				ret += 1
        			if j == 0 or grid[i][j-1] == 0:
        				ret += 1
        			if j == len(grid[i])-1 or grid[i][j+1] == 0:
        				ret += 1
        return ret 

        
