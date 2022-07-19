class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = 0
        result = []
        
        for i, n in enumerate(nums):
            res = nums[i] + prefix
            result.append(res)
            prefix = res
        
        return result