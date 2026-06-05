class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def dfs(m, n):
            if (m, n) in memo:
                return memo[(m, n)]

            if m + n == len(s3):
                return True

            ans = False
            currIdx = m + n

            if m < len(s1) and s1[m] == s3[currIdx]:
                ans = ans or dfs(m + 1, n)

            if n < len(s2) and s2[n] == s3[currIdx]:
                ans = ans or dfs(m, n + 1)

            memo[(m, n)] = ans
            return ans

        return dfs(0, 0)