class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,j = 0,len(nums)-1
        result=[]
        while i<=j:
            if (nums[i]**2) <=  (nums[j]**2):
                result.append(nums[j]**2)
                j-=1
            else:
                result.append(nums[i]**2)
                i+=1
        i,j = 0,len(nums)-1
        while i<j:
            result[i],result[j] = result[j],result[i]
            i+=1
            j-=1

        return result         
        