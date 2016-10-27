class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) == 0:
        	return 0
        vis = [[0 for j in range(len(heightMap[0]))] for i in range(len(heightMap))]
        import heapq
        ret = 0
        cx = [-1,0,1,0]
        cy = [0,1,0,-1]
        for i in range(1, len(heightMap)-1):
        	for j in range(1, len(heightMap[0])-1):
        		if vis[i][j] == 0:
        			queue = [(heightMap[i][j], i, j)]
        			cnt = 0
        			wall_height = 0
        			while len(queue) > 0:
        				top = heapq.heappop(queue)
        				height, x, y = top
        			
        				ret += cnt * (height - wall_height)
        				cnt += 1
        				wall_height = height
        				if x==0 or x==len(heightMap)-1 or y==0 or y==len(heightMap[0])-1:
        					break
        				tag = 1
        				for t in range(4):
        					tx = x + cx[t]
        					ty = y + cy[t]
        					if heightMap[tx][ty] < height and vis[tx][ty]==0:
        						tag = 0
        						break
        					heapq.heappush(queue, (heightMap[tx][ty], tx, ty))
        				if tag == 0:
        					break
        				vis[x][y] = 1
        return ret

print Solution().trapRainWater([
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
])