class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        r, c = 0, 0
        max_r, max_c = len(mat), len(mat[0])
        all_items = max_r * max_c
        visited = [[False for _ in range(max_c)] for _ in range(max_r)]
        res = []
        direction = "right"
        
        while len(res) < all_items:
            res.append(mat[r][c])
            visited[r][c] = True
            if direction == "right":
                if c < max_c - 1 and not visited[r][c+1]:
                    c += 1
                else:
                    # go down
                    r += 1
                    direction = "down"
            elif direction == "down":
                if r < max_r - 1 and not visited[r+1][c]:
                    r += 1
                else:
                    # go left
                    c -= 1
                    direction = "left"
            elif direction == "left":
                if c > 0 and not visited[r][c-1]:
                    c -= 1
                else:
                    # go up
                    r -= 1
                    direction = "up"
            elif direction == "up":
                if r > 0 and not visited[r-1][c]:
                    r -= 1
                else:
                    # go right
                    c += 1
                    direction = "right"

        return res