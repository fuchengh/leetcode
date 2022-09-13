class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = defaultdict(lambda: 0)
        if len(s) != len(t):
            return False
        
        for c in s:
            table[c] += 1
        
        for c in t:
            if table[c] > 0:
                table[c] -= 1
            else:
                return False
        
        return True