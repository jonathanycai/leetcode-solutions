class Solution:
    def checkValidString(self, s: str) -> bool:
        minB, maxB = 0, 0

        for c in s:
            if c == "(":
                minB += 1
                maxB += 1
            elif c == ")":
                minB -= 1
                maxB -= 1
            else:
                minB -= 1
                maxB += 1
            
            if minB < 0:
                minB = 0
            
            if maxB < 0:
                return False

            print(minB)
        
        return minB == 0