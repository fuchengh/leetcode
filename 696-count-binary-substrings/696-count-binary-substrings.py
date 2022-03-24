class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                group.append(1)
            else:
                group[-1] += 1
        res = 0
        for g in range(len(group)-1):
            this_group = group[g]
            next_group = group[g+1]
            res += min(this_group, next_group)
        
        return res