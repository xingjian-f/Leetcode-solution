class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones) == 1:
            return True
        stack = []
        if stones[1] == 1:
            stack.append((1,1))
        vis = set((1,1))
        while len(stack) > 0:
            pos, step = stack.pop()
            if pos == len(stones)-1:
                return True
            for i in range(pos+1, len(stones)):
                gap = stones[i]-stones[pos]
                if step+1 < gap:
                    break
                for t in [-1,0,1]:
                    t_step = step+t 
                    if t_step == gap and (i, gap) not in vis:
                        vis.add((i,gap))
                        stack.append((i, gap))
        return False



print Solution().canCross([0,1,3,5,6,8,12,17])