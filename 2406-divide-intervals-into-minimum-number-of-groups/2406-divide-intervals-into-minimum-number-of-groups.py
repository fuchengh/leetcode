class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pq = [intervals[0][1]]
        
        for intv in intervals[1:]:
            if pq[0] < intv[0]:
                heappop(pq)
                heappush(pq, intv[1])
            else:
                heappush(pq, intv[1])
        
        return len(pq)