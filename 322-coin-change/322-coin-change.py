class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] * (amount+1) # stores best number of coins to create val = i
        
        for i in range(1, amount+1):
            dp[i] = math.inf
            for c in coins:
                if i - c < 0:
                    break
                if dp[i-c] != math.inf: # has been processed
                    dp[i] = min(dp[i], 1 + dp[i-c]) # use dp[i-c] + c(1) coins
        
        return dp[-1] if dp[-1] != math.inf else -1
        