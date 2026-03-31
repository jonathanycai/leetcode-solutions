class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        corr = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, curr):
            if i == len(digits):
                res.append(curr)
                return
            
            options = corr[digits[i]]
            for l in options:
                dfs(i + 1, curr + l)
            
            return

        dfs(0, "")

        return res if digits else []