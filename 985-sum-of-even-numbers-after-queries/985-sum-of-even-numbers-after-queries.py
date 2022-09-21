class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = 0
        for n in nums:
            if n % 2 == 0:
                even += n
        
        res = []
        
        for q in queries:
            val, idx = q
            if nums[idx] % 2 != 0:
                if (nums[idx] + val) % 2 == 0:
                    # odd -> even
                    even += nums[idx] + val
                    res.append(even)
                else:
                    # odd -> odd
                    res.append(even)
            else:
                if (nums[idx] + val) % 2 == 0:
                    # even -> even
                    even += val
                    res.append(even)
                else:
                    # even -> odd
                    even -= nums[idx]
                    res.append(even)
            nums[idx] += val
        
        return res