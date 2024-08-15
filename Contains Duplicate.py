class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        for i in nums:
            if i in hashset:
                return True
            hashset[i] = i
        return False