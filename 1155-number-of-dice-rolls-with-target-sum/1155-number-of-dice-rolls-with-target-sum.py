class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @lru_cache(None)
        def dfs(dices, remain):
            if dices == 0 and remain == 0:
                return 1
            if dices < 0 or remain < 0:
                # cannot use this result
                return 0
            res = 0
            
            for i in range(1, k+1): # k faces for each dice
                if i > remain:
                    break
                # use one dice, subtract remain by i
                res += dfs(dices - 1, remain - i)
            
            return res % (10**9+7)
        
        return dfs(n, target)