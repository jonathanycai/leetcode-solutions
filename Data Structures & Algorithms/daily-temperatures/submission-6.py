class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[] # [index, temp]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                prevI, prevT = stack.pop()
                res[prevI] = i - prevI
            
            stack.append((i, t))
        
        return res