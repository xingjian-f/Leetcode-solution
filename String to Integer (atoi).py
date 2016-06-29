class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        posl = -1
        posr = -1
        for i in range(len(s)):
        	if posl == -1 and s[i] != ' ':
        		posl = i
        		posr = i  
        	elif posl != -1:
        		if s[i].isdigit() == False:
        			break
        		else:
        			posr = i 

        if posl == -1:
        	return 0

        s = s[posl:posr+1]
        try:
        	x = int(s)
        except:
        	x = 0
        x = min(x, 2147483647)
        x = max(x, -2147483648)
       	return x