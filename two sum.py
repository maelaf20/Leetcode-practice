class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashset:
                return [i,hashset[complement]]
            hashset[nums[i]] = i
        return []