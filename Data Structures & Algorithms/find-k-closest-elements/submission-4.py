class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        
        l, r = 0, len(arr) - 1
        res = []

        while r - l >= k:
            distL = abs(arr[l] - x)
            distR = abs(arr[r] - x)

            if distL > distR:
                l += 1
            else:
                r -= 1
            
        return arr[l: r + 1]