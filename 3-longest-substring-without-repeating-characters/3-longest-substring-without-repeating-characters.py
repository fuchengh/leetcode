class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        ans = 0
        seen = {}
        
        while right < len(s):
            if s[right] in seen:
                left = max(seen[s[right]], left)
            ans = max(ans, right-left+1)
            seen[s[right]] = right+1
            right += 1
        return ans