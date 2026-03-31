class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start, spend = 0, 0
        for i in range(len(gas)):
            spend += (gas[i] - cost[i])

            if spend < 0:
                start = i + 1
                spend = 0
        
        return start