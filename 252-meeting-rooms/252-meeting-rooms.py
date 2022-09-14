class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        for i in range(1, len(intervals)):
            prev_end = intervals[i-1][1]
            curr_start = intervals[i][0]
            
            if curr_start < prev_end:
                return False
        
        return True
            