class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x: x[1])
        if len(points) == 0:
        	return 0
        last_shot = points[0][1]
        ret = 1
        for i in points:
        	left, right = i 
        	if left <= last_shot:
        		continue
        	else:
        		ret += 1
        		last_shot = right
        return ret 

       