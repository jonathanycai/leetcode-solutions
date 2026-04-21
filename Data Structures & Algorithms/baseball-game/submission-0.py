class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for c in operations:
            if c == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                ans = num1 + num2
                stack.append(ans)
            elif c == "C":
                stack.pop()
            elif c == "D":
                num = stack[-1] * 2
                stack.append(num)
            else:
                stack.append(int(c))
            print(stack)
        
        return sum(stack)
                
