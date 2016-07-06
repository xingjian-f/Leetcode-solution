class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        posl = 0
        for i in range(1, len(height)):
        	if height[i] >= height[posl]:
        		for j in range(posl+1, i):
        			ans += height[posl]-height[j]
        		posl = i
        if posl != len(height):
        	height = height[posl:][::-1]
        # print height
        posl = 0
        for i in range(1, len(height)):
        	if height[i] >= height[posl]:
        		for j in range(posl+1, i):
        			ans += height[posl]-height[j]
        		posl = i
        print ans
        return ans

Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])