class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(None)
        def recurse(idx, s):
            if idx == len(s):
                return 1
            if s[idx] == '0':
                return 0
            if idx == len(s)-1:
                return 1
            # read next one char
            ans = recurse(idx+1, s)
            if int(s[idx:idx+2]) <= 26: # try to read next two char
                ans += recurse(idx+2, s)
            
            return ans
    
        return recurse(0, s)