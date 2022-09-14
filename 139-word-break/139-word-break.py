class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for right in range(1, len(s)+1):
            for left in range(right):
                if s[left:right] in wordDict and dp[left]:
                    dp[right] = True
                    break
        return dp[-1]