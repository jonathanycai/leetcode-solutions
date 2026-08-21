class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        left, right = 0, n
        top, bottom = 0, n
        curr = 1

        while left < right and top < bottom:
            for i in range(left, right):
                res[top][i] = curr
                curr += 1
            top += 1
            for i in range(top, bottom):
                res[i][right - 1] = curr
                curr += 1
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res[bottom - 1][i] = curr
                curr += 1
            bottom -=1
            for i in range(bottom - 1, top - 1, -1):
                res[i][left] = curr
                curr += 1
            left += 1
        
        return res