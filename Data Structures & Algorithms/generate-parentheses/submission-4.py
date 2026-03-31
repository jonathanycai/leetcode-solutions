class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, curr):
            if l == n and r == n:
                res.append(curr) 
                return
            
            if l < n:
                dfs(l + 1, r, curr + "(")
            if r < l:
                dfs(l, r + 1, curr + ")")
        
        dfs(1, 0, "(")
        return res 