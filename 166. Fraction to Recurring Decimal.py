class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator*denominator == 0:
        	return '0'
        tag = 1 if numerator*denominator > 0 else -1
        numerator = abs(numerator)
        denominator = abs(denominator)
        int_res = numerator / denominator
        numerator = numerator % denominator
        if numerator == 0:
        	return str(tag * int_res)

        numerator = numerator * 10
        denominator = denominator
        ret = []
        used = {str(numerator):0}
        recurent_len = -1

        while numerator > 0:
        	ret.append(str(numerator / denominator))
        	numerator = (numerator % denominator) * 10
        	if str(numerator) in used:
        		recurent_len = used[str(numerator)]
        		break
        	else:
        		used[str(numerator)] = len(ret)
        if recurent_len != -1:
        	ret.insert(recurent_len, '(')
        	ret = str(int_res) + '.' + ''.join(ret) + ')'
        else:
        	ret = str(int_res) + '.' + ''.join(ret)
        if tag == -1:
        	ret = '-' + ret 
        return ret

print Solution().fractionToDecimal(-64, 7)