class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        for idx, char in enumerate(s):
            # special cases
            if char == "I" and idx+1 < len(s) and s[idx+1] in {"V", "X"}:
                ans -= 1
                continue
            if char == "X" and idx+1 < len(s) and s[idx+1] in {"L", "C"}:
                ans -= 10
                continue
            if char == "C" and idx+1 < len(s) and s[idx+1] in {"D", "M"}:
                ans -= 100
                continue
            
            ans += table[char]
        
        return ans