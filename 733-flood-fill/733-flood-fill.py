class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        q = deque([(sr, sc)])
        orig_color = image[sr][sc]
        
        while q:
            cur = q.popleft()
            x, y = cur
            seen.add((x, y))
            image[x][y] = color
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                if (x+dx, y+dy) not in seen \
                and 0 <= x+dx < len(image) \
                and 0 <= y+dy < len(image[0]) \
                and image[x+dx][y+dy] == orig_color:
                    q.append((x+dx, y+dy))
        return image