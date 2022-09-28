class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = -1
        right = 0
        ans = 0
        seen = defaultdict(lambda: -1)
        
        while right < len(s):
            if seen[s[right]] > left: # we have seen s[right] before, update left
                left = seen[s[right]]
            seen[s[right]] = right
            ans = max(ans, right-left)
            right += 1
            
        return ans