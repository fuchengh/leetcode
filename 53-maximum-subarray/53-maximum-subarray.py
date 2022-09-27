class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = nums[0]
        
        for n in nums[1:]:
            cur = max(n, cur + n)
            ans = max(ans, cur)
        
        return ans