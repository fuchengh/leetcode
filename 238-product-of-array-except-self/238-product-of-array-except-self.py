class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [1]
        R = [1]
        
        # Build Left array (prefix array of each idx)
        for i in range(1, len(nums)):
            L.append(L[i-1] * nums[i-1])
        
        # Build right array (suffix array of each idx)
        for i in range(1, len(nums)):
            R.append(R[i-1] * nums[len(nums) - i])
        
        R = R[::-1]
        ans = []
        
        for i in range(len(L)):
            ans.append(L[i] * R[i])
        
        return ans