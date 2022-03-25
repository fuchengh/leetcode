class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        strs = defaultdict(lambda: 1)
        seen = set()
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] in seen:
                    strs[j-i+1] += 1
                else:
                    seen.add(s[i:j+1])
        
        keys = sorted(strs.keys())[::-1]
        for i in keys:
            if strs[i] > 1:
                return i
        return 0