class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = -math.inf
        min_price = math.inf
        
        for p in prices:
            if min_price > p:
                min_price = p
            
            cur_profit = p - min_price
            
            if cur_profit > ans:
                ans = cur_profit
        
        return ans