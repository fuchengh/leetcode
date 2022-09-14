class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        seen = defaultdict(lambda: 0) # remember last seen index of chars
        
        for right in range(len(s)):
            if s[right] in seen and left <= seen[s[right]]:
                # update left to next char after this
                left = seen[s[right]] + 1
            else:
                ans = max(ans, right - left + 1)
        
            seen[s[right]] = right
        
        return ans