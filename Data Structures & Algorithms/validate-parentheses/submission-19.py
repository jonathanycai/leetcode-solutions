class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brac = {")" : "(", "]" : "[", "}" : "{"}

        for b in s:
            if b in brac:
                if stack and stack[-1] == brac[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        
        return True if len(stack) == 0 else False