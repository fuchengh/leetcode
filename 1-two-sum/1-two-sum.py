class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(lambda: -1)
        
        for idx, n in enumerate(nums):
            comp = target - n
            if seen[comp] >= 0:
                return [idx, seen[comp]]
            seen[n] = idx