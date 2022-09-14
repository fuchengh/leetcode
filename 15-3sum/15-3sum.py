class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(target, cur, ptr):
            seen = set()
            res = []
            while ptr < len(nums):
                complement = target - nums[ptr]
                if complement in seen:
                    res.append([cur, nums[ptr], complement])
                    while ptr+1 < len(nums) and nums[ptr] == nums[ptr+1]:
                        # skipping duplicate values since we already calculate it
                        ptr += 1
                seen.add(nums[ptr])
                ptr += 1
                
            return res
            
        ans = []
        nums.sort()
        
        for i, n in enumerate(nums):
            if n > 0:
                break
            remain = 0 - n
            if i == 0 or nums[i-1] != nums[i]:
                # also skipps duplicate values
                find = twoSum(remain, n, i+1)
                if find:
                    ans.extend(find)
        return ans