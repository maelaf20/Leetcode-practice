class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        final = []
        for i in range(0,len(candies)):
            if (candies[i]+extraCandies) >= max(candies):
                final.append(True)
            else:
                final.append(False)
        return final
        
        