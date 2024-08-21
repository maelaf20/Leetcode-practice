
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            
            l, r = i + 1, n - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                else:
                    return current_sum  # Exact match found

        return closest_sum