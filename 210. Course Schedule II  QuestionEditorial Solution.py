class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        in_degree = [0 for i in xrange(numCourses)]
        edges = [[] for i in xrange(numCourses)]
        for i in prerequisites:
        	to_id, from_id = i 
        	edges[from_id].append(to_id)
        	in_degree[to_id] += 1

        queue = []
        for i in xrange(numCourses):
        	if in_degree[i] == 0:
        		queue.append(i)

        ret = []
        while len(queue) > 0:
        	top = queue.pop()
        	ret.append(top)
        	for nei in edges[top]:
        		in_degree[nei] -= 1
        		if in_degree[nei] == 0:
        			queue.append(nei)
        if len(ret) == numCourses:
        	return ret 
        else:
        	return []


print Solution().findOrder(2, [[0, 1], [1, 0]])