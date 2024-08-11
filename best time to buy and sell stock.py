class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i,j = 0,1
        while j<len(prices):
            price = prices[j]-prices[i]
            maxProfit = max(maxProfit,price)
            if prices[i]>prices[j]:
                i=j
                j+=1
            else:
                j+=1
        return maxProfit