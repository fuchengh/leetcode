class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r, c):
            s = [(r, c)]
            seen.add((r, c))
            while s:
                cur = s.pop()
                x, y = cur
                for nr, nc in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= nr < len(grid) \
                    and 0 <= nc < len(grid[0]) \
                    and (nr, nc) not in seen \
                    and grid[nr][nc] == "1":
                        s.append((nr, nc))
                        seen.add((nr, nc))
        
        ans = 0
        seen = set()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in seen and grid[r][c] == "1":
                    ans += 1
                    bfs(r, c)
        
        return ans