class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = defaultdict(lambda: [])
        visited = [0 for _ in range(numCourses)]
        
        for pre in prerequisites:
            c, p = pre
            course_dict[p].append(c)
        
        
        def dfs(i):
            if visited[i] == -1: return False # found a cycle
            if visited[i] == 1: return True # if this node has already perform dfs, skip it
            visited[i] = -1 # first mark this node as visited, and start dfs
            for j in course_dict[i]:
                if not dfs(j): return False
            visited[i] = 1 # after performing dfs, mark the node as done
            return True
    
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True