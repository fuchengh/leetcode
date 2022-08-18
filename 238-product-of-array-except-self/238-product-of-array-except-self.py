class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # use ans as L array (prefix array)
        ans = [1] * len(nums)
        
        for i in range(1, len(nums)):
            ans[i] = nums[i-1] * ans[i-1]
            
        # calcualte suffix array (store as right)
        right = 1
        for i in range(len(nums)):
            ans[len(nums)-i-1] *= right
            right *= nums[len(nums)-i-1]
        
        return ans