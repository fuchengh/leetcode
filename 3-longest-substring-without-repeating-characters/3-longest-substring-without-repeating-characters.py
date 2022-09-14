class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        seen = defaultdict(lambda: 0) # remember last seen index of chars
        
        for right, char in enumerate(s):
            if s[right] in seen and left <= seen[char]:
                # update left to next char after this
                left = seen[char] + 1
            else:
                ans = max(ans, right - left + 1)
        
            seen[char] = right
        
        return ans