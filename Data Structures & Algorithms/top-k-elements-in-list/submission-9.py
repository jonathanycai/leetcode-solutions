class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        buckets = [[] for _ in range(len(nums) + 1)]
        counter = Counter(nums)

        for item, val in counter.items():
            buckets[val].append(item)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            for item in bucket:
                res.append(item)
                k -= 1
                if k == 0:
                    return res