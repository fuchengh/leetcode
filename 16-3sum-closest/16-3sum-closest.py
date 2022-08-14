class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = math.inf
        ans = math.inf
        
        for i in range(len(nums)):
            lo = i+1
            hi = len(nums)-1
            
            while lo < hi:
                sum = nums[lo] + nums[hi] + nums[i]
                if abs(sum - target) < closest:
                    closest = abs(sum - target)
                    ans = sum
                
                if sum < target:
                    lo += 1
                elif sum == target:
                    return target
                else:
                    hi -= 1
        
        return ans