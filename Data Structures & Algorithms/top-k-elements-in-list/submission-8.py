class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        seen = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            seen[n] += 1

        for key, val in seen.items():
            buckets[val].append(key)
        
        res = []
        for i in range(len(nums), -1, -1):
            currBucket = buckets[i]
            for n in currBucket:
                res.append(n)
                k -= 1
                if k == 0:
                    return res
        
        return res
            


