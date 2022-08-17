class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(lambda: 0)
        
        for n in nums:
            freq[n] += 1
        
        freq_list = list(zip(freq.keys(), freq.values()))
        freq_sorted = sorted(freq_list, key=lambda x: x[1])[::-1]
        
        ans = []
        
        for i in range(k):
            ans.append(freq_sorted[i][0])
        
        return ans