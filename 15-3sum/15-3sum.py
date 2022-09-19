class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        def twoSum(cur, target, left):
            seen = set()
            res = []
            
            while left < len(nums):
                comp = target - nums[left]
                if comp in seen:
                    res.append([cur, nums[left], comp])
                    while left+1 < len(nums) and nums[left] == nums[left+1]:
                        left += 1
                seen.add(nums[left])
                left += 1 
                
            return res
    
        res = []
        cur = 0
        while cur < len(nums):
            n = nums[cur]
            if n > 0:
                break
            if cur == 0 or nums[cur] != nums[cur-1]:
                res.extend(twoSum(n, -n, cur+1))
            cur += 1
            
        return res