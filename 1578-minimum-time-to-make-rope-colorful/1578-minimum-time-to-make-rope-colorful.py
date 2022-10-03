class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        i, j = 0, 0
        
        while i < len(neededTime) and j < len(neededTime):
            group_total = 0
            group_max = 0
            
            while j < len(neededTime) and colors[i] == colors[j]:
                # keep the sum of the group and the largest one
                group_total += neededTime[j]
                group_max = max(group_max, neededTime[j])
                j += 1
            
            # delete all ballons that are not the largest one
            total_time += group_total - group_max
            i = j # move to next group
        
        return total_time