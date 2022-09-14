class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def helper(left):
            if left == len(s):
                return True
            for end in range(left+1, len(s)+1):
                if s[left:end] in wordDict and helper(end):
                    return True
            return False
        
        return helper(0)