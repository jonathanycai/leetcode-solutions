class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        ans = [0] * 2
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i

        return []
