class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        b = int(''.join(map(str, b)))
        Mod = 1337
        mod_res = []
        vis = set()
        tem = 1
        while True:
        	tem = (tem * a) % Mod 
        	if tem in vis:
        		break
        	vis.add(tem)
        	mod_res.append(tem)

        rec_len = len(vis)
        print mod_res
        return mod_res[(b-1)%rec_len]

print Solution().superPow(2 ,[2,0])