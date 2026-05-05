class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)

        def dfs(remainder):
            if remainder == 0:
                return 1
            if remainder < 0:
                return 0
            if memo[remainder]:
                return memo[remainder]
            
            total = 0
            for n in nums:
                total += dfs(remainder - n)
            
            memo[remainder] = total
            return total
        
        return dfs(target)