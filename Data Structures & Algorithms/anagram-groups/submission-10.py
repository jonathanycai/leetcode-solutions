class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                freq[idx] += 1
            
            groups[tuple(freq)].append(s)
        
        return list(groups.values())