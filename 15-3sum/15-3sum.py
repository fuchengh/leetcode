class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(arr, remain, res):
            lo = 0
            hi = len(arr)-1
            
            while lo < hi:
                sum = arr[lo] + arr[hi] + remain
                
                if sum < 0:
                    lo += 1
                elif sum > 0:
                    hi -= 1
                else:
                    res.append([remain, arr[lo], arr[hi]])
                    lo += 1
                    hi -= 1
                    
                    while lo < hi and arr[lo] == arr[lo-1]:
                        lo += 1
        res = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if nums[i] > 0: break
            if nums[i-1] != nums[i] or i == 0:
                twoSum(nums[i+1:], nums[i], res)
        
        return res