class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {} #(i, )
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(m , n):
            if (m, n) in memo:
                return memo[(m, n)]
            
            if m + n == len(s3):
                return True
            
            currIdx = m + n

            ans = False
            if m < len(s1) and s3[currIdx] == s1[m]:
                ans |= dfs(m + 1, n)
            if n < len(s2) and s3[currIdx] == s2[n] and n < len(s2):
                ans |= dfs(m, n + 1)
            
            memo[(m, n)] = ans
            
            return memo[(m, n)]
        
        return dfs(0, 0)
            
