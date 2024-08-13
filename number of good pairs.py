class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i in nums:
            numcount = nums.count(i)
            valid = numcount*(numcount-1)//2
            pairs+= valid
            nums = [num for num in nums if num!= i]
        return pairs
    