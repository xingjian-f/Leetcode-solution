class Solution(object):
    def lexicalOrder(self, n):
	    top = 1
	    while top * 10 <= n:
	        top *= 10
	    def mycmp(a, b, top=top):
	        while a < top: a *= 10
	        while b < top: b *= 10
	        return -1 if a < b else b < a
	    return sorted(xrange(1, n+1), mycmp)


print Solution().lexicalOrder(100)