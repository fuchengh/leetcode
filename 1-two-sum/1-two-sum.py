class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        
        for idx, n in enumerate(nums):
            remain = target - n
            if remain in table:
                return [table[remain], idx]
            table[n] = idx
        
        