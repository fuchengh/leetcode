class Solution:

    def __init__(self, w: List[int]):
        self.candidates = []
        prefix_sum = 0
        # duplicate index by weight
        for weight in w:
            prefix_sum += weight
            self.candidates.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target =  random.random() * self.total_sum
        for i, prefix_sum in enumerate(self.candidates):
            if target < prefix_sum:
                return i
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()