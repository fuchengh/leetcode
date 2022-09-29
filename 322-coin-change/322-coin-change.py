class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = defaultdict(lambda: None)
        
        @lru_cache(None)
        def dfs(target):
            if target < 0:
                return -1
            if target == 0:
                return 0
            min_cost = math.inf
            for c in coins:
                res = dfs(target - c)
                if res != -1:
                    min_cost = min(min_cost, res+1)
            return min_cost if min_cost != math.inf else -1
    
        return dfs(amount)