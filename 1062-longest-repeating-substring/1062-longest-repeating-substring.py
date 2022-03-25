class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        def search(n, length): # search substring of a given length
            seen = set()
            for start in range(n - length + 1):
                if s[start:start+length] in seen:
                    return start
                seen.add(s[start:start+length])
            
            return -1
    
        n = len(s)
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if search(n, mid) != -1:
                left = mid + 1
            else:
                right = mid - 1
                
        return left - 1