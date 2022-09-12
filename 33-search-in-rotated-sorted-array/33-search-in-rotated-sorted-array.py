class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            elif nums[mid] > nums[start]:
                # left array is sorted
                if target >= nums[start] and target < nums[mid]:
                    # search left subarray
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # right array is sorted
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        # othersiwe, not found
        return -1
            