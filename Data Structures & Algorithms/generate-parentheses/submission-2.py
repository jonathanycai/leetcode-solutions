class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(curr, l, r):
            if r > l:
                return
            if l ==n and r ==n:
                res.append(curr)
                return
            
            if l < n:
                dfs(curr + "(", l + 1, r)
            
            if r < l:
                dfs(curr + ")", l, r + 1)
        
        dfs("(", 1, 0)

        return res