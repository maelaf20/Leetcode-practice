class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            midNumber = nums[mid]
            if target>midNumber:
                left = mid+1
            elif target<midNumber:
                right = mid-1
            else:
                return mid
        return -1
            
        