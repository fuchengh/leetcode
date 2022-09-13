class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        hasOdd = False
        
        for _, v in freq.items():
            ans += v // 2 * 2
            
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans