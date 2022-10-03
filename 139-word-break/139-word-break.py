class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        
        @lru_cache(None)
        def dfs(start):
            if start == len(s):
                return True
            
            for end in range(start+1, len(s)+1):
                word = s[start:end]
                # can reach the end starting with current word
                if word in wordSet and dfs(end):
                    return True
            return False
        
        return dfs(0)