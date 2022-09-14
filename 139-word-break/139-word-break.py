class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = defaultdict(lambda: False)
        words = set(wordDict)
        
        def helper(left):
            if left == len(s):
                return True
            if left in seen:
                return seen[left]
            for right in range(left+1, len(s)+1):
                cur = s[left:right]
                if cur in words and helper(right):
                    seen[left] = True
                    return True
            seen[left] = False
            return False
        
        return helper(0)