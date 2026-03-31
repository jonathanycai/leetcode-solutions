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

        def combinations(i, curr):
            
            if i >= len(digits):
                res.append(curr)
                return
            
            currChar = digits[i]
            options = corr[currChar]

            for c in options:
                combinations(i + 1, curr + c)

        if digits:
            combinations(0, "")
        
        return res