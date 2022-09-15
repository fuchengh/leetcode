class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        freq = Counter(changed)
        ans = []
        
        for n in changed:
            if freq[n] > 0:
                freq[n] -= 1
                if freq[2 * n] > 0:
                    freq[2*n] -= 1
                    ans.append(n)
        
        return ans if len(ans) == len(changed)//2 else []