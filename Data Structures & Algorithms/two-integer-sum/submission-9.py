class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for n in range(len(nums)):
            remainder = target - nums[n]
            if remainder in dictionary:
                return [dictionary.get(remainder), n]
            dictionary[nums[n]] = n
        return -1