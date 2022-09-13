class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def dfs(r, c, newColor):
            seen = set()
            color = image[r][c]
            s = [(r, c)]
            
            while s:
                cur = s.pop()
                i, j = cur
                image[i][j] = newColor
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == color \
                        and (x, y) not in seen:
                        s.append((x, y))
                        seen.add((x, y))
        
        dfs(sr, sc, newColor)
        return image