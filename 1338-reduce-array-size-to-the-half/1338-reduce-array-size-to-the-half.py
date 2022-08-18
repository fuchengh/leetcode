class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        size = len(arr)
        target = len(arr) / 2
        
        table = defaultdict(lambda: 0)
        
        for n in arr:
            table[n] += 1
        
        freq = sorted(list(zip(table.keys(), table.values())), key=lambda x: x[1])[::-1]
        
        ans = 0
        sum = 0
        i = 0
        
        while sum < target:
            sum += freq[i][1]
            ans += 1
            i += 1
        
        return ans