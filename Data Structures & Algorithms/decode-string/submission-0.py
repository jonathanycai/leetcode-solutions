class Solution:
    def decodeString(self, s: str) -> str:
        strStack = []
        countStack = []
        curr = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                strStack.append(curr)
                countStack.append(k)
                curr = ""
                k = 0
            elif c == "]":
                temp = curr
                curr = strStack.pop()
                count = countStack.pop()
                curr += temp * count
            else:
                curr += c
        
        return curr