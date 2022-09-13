# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        start = 0
        end = n
        
        while start <= end:
            mid = (start + end) // 2
            
            if isBadVersion(mid):
                if mid == 0 or (isBadVersion(mid) and not isBadVersion(mid-1)):
                    return mid
                else:
                    end = mid - 1
            else:
                start = mid + 1
        
        