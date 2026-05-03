class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        size = 0
        res = 0
        sign = -1 # 0 is less, 1 is greater

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                size = size + 1 if sign == 0 else 1
                sign = 1
            elif arr[i] < arr[i + 1]:
                size = size + 1 if sign == 1 else 1
                sign = 0
            else:
                size = 0
                sign = -1

            res = max(res, size)
        
        return res + 1

