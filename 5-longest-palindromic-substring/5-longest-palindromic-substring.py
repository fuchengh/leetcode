class Solution:
    def longestPalindrome(self, s: str) -> str:
        # build dp table
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = ""
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j] and (j - i == 1 or dp[i+1][j-1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False
                if dp[i][j] and j-i + 1 > len(res):
                    res = s[i:j+1]
        return res