class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = defaultdict(lambda: 0)
        
        for c in magazine:
            table[c] += 1
        
        for c in ransomNote:
            if table[c] == 0:
                return False
            else:
                table[c] -= 1
        
        return True