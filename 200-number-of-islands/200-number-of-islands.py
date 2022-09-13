class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        
        def dfs(r, c):
            q = [(r, c)]
            
            while q:
                cur = q.pop()
                i, j = cur
                
                for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                        # mark this element as 0
                        grid[x][y] = "0"
                        q.append((x, y))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        
        return ans