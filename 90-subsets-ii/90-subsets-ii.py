class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, path, res):
            res.append(path[:])
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue # skip duplicate
                path.append(nums[i])
                backtrack(i+1, path, res)
                path.pop()
        
        res = []
        path = []
        nums.sort()
        backtrack(0, path, res)
        
        return res