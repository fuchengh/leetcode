class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = -math.inf
        local_min = math.inf
        
        for p in prices:
            if p < local_min:
                local_min = p
            
            profit = p - local_min
            
            if profit > maxprofit:
                maxprofit = profit
            
        return maxprofit
            