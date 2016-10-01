class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        pq = [(people[i][1], people[i][0], i) for i in range(len(people))]
        for _ in range(len(people)):
        	# print pq 
        	front, val, idx = 1e9, None, None
        	for i in pq:
        		if i[0] < front:
        			front, val, idx = i 
        		elif i[0] == front and i[1] < val:
        			front, val, idx = i 
        	# print front, val, idx 
        	ret.append(people[idx])
        	tem_pq = []
        	for i in pq:
        		tem_front, tem_val, tem_idx = i 
        		if idx == tem_idx:
        			continue
        		# print tem_val, val, idx not in vis
        		if tem_val <= val:
        			tem_front -= 1
        			# print tem_front, tem_val, tem_idx
        		tem_pq.append((tem_front, tem_val, tem_idx))
        	pq = tem_pq
        return ret 

# print Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
