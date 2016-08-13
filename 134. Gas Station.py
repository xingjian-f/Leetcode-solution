class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        new_gas = [0]
        new_cost = [0]
        new_gas.extend(gas)
        new_cost.extend(cost)
        new_gas.extend(gas[:-1])
        new_cost.extend(cost[:-1])
        
        gas = range(len(new_gas))
        cost = range(len(new_cost))
        gas[0] = 0
        cost[0] = 0
        for pos in range(1, len(new_cost)):
        	gas[pos] = gas[pos-1] + new_gas[pos]
        	cost[pos] = cost[pos-1] + new_cost[pos]
        posl = 0
        posr = 1
        while posr < len(new_cost):
        	if gas[posr] - gas[posl] >= cost[posr] - cost[posl]:
        		if posr - posl == n:
        			return posl
        		posr += 1
        	else:
        		posl += 1
        		posr = max(posr, posl+1)
        return -1



print Solution().canCompleteCircuit([1,2,3],[3,2,2])