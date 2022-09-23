class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        local_min = math.inf
        
        for p in prices:
            if p < local_min:
                local_min = p
            ans = max(ans, p - local_min)
        
        return ans