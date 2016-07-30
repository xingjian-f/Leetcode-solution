class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        vis = set(['0' * n])
        ans = [0]
        last = [0] * n
        while True:
            tag = 0
            for i in range(n):
                last[-i-1] = 1 - last[-i-1]
                str_last = ''.join(map(str,last))
                if str_last not in vis:
                    vis.add(str_last)
                    tag = 1
                    ans.append(int(str_last,2))
                    break
                else:
                    last[-i-1] = 1 - last[-i-1]
            if tag == 0:
                break
        return ans