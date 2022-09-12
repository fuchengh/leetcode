class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = math.inf
        maxprofit = 0
        
        for p in prices:
            if p < minprice:
                minprice = p
            elif p - minprice > maxprofit:
                maxprofit = p - minprice
    
        return maxprofit