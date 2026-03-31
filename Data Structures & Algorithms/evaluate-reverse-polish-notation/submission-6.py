class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])

        for t in tokens:
            if t == "+":
                x = int(stack.pop())
                y = int(stack.pop())
                ans = y + x
                stack.append(ans)
            elif t == "-":
                x = int(stack.pop())
                y = int(stack.pop())
                ans = y - x
                stack.append(ans)
            elif t == "*":
                x = int(stack.pop())
                y = int(stack.pop())
                ans = y * x
                stack.append(ans)
            elif t == "/":
                x = int(stack.pop())
                y = int(stack.pop())
                ans = y / x
                stack.append(ans)
            else:
                stack.append(t)
        
        return int(stack[-1])