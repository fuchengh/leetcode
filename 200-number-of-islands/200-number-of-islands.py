class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        ans = 0
        
        def dfs(i, j):
            q = deque([(i, j)])
            while q:
                cur = q.pop()
                seen.add(cur)
                left = [cur[0], cur[1]-1]
                right = [cur[0], cur[1]+1]
                up = [cur[0]-1, cur[1]]
                down = [cur[0]+1, cur[1]]
                
                for r, c in [left, right, up, down]:
                    if 0 <= r < len(grid)\
                    and 0 <= c < len(grid[0]) \
                    and grid[r][c] == "1"\
                    and (r, c) not in seen:
                        q.append((r, c))
                
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    # add number of islands
                    ans += 1
                    # start bfs
                    dfs(i, j)
        return ans