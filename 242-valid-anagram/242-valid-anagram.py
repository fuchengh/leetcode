class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = defaultdict(lambda: 0)
        
        for c in s:
            table[c] += 1
        
        for c in t:
            if table[c] == 0:
                return False
            table[c] -= 1
        
        return True and len(s) == len(t)