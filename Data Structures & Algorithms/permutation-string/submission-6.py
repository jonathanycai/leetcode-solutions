class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = {}
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
        
        count = {}
        l = 0
        for r in range(len(s2)):
            count[s2[r]] = count.get(s2[r], 0) + 1
            if (r - l + 1) == len(s1):
                if count == s1Count:
                    return True
                else:
                    count[s2[l]] = count.get(s2[l], 0) - 1
                    if count[s2[l]] == 0:
                        count.pop(s2[l])
                    l += 1
        
        return False

        
        