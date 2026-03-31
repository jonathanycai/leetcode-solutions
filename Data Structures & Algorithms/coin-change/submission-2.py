class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def dfs(tot):
            if tot in mem:
                return mem[tot]
            if tot == 0:
                return 0
            
            res = float("inf")
            for c in coins:
                if tot - c >= 0:
                    res = min(dfs(tot - c) + 1, res)
            
            mem[tot] = res
            return res
        
        ways = dfs(amount)
        return ways if ways < float("inf") else -1
