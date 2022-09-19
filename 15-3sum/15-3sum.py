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
                seen.add(nums[left])
                left += 1 
                
            return res
    
        res = set([])
        cur = 0
        while cur < len(nums):
            n = nums[cur]
            tmp = twoSum(n, -n, cur+1)
            for r in tmp:
                res.add(tuple(r))
            cur += 1
            while cur+1 < len(nums) and nums[cur-1] == nums[cur]:
                cur += 1
            
        return [list(x) for x in res]