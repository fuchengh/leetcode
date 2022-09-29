class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        
        left = 0
        right = len(arr)-k
        
        while left < right:
            mid = (left+right) // 2
            
            if arr[mid+k] - x < x - arr[mid]:
                # right is closer to x
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left+k]