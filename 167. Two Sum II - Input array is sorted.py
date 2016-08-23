class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        posl = 0
        posr = len(numbers)-1
        while posl < posr:
        	total = numbers[posl] + numbers[posr]
        	if total == target:
        		return [posl+1, posr+1]
        	elif total < target:
        		posl += 1
        	else:
        		posr -= 1
        