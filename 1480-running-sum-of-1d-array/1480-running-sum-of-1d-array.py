class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0
        
        for i, n in enumerate(nums):
            nums[i] += prev
            prev = nums[i]
        
        return nums