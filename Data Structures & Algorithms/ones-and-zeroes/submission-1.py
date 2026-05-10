class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}

        def dfs(i, z, o):
            if i == len(strs):
                return 0
            
            if (i, z, o) in dp:
                return dp[(i, z, o)]
            
            zeroes = strs[i].count("0")
            ones = strs[i].count("1")

            skip = dfs(i + 1, z, o)
            take = 0

            if zeroes <= z and ones <= o:
                take = 1 + dfs(i + 1, z - zeroes, o - ones)
            
            dp[i, z, o] = max(skip, take)
            return dp[i, z, o]
        
        return dfs(0, m, n)