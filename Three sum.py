class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                endsum = nums[l]+nums[r]+nums[i]
                if endsum == 0:
                    final.append( [nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif endsum >0:
                    r-=1
                else:
                    l+=1
                    
        return final

