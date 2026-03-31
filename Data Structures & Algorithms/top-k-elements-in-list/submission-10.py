class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        freq = [[] for _ in range(len(nums) + 1)]
        for key, val in count.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res
        
        return res
