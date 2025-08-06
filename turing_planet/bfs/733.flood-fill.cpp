/*
 * @lc app=leetcode id=733 lang=cpp
 *
 * [733] Flood Fill
 */

// @lc code=start
class Solution
{
  public:
#define VALID(i, j, maxi, maxj) ((i >= 0 && j >= 0 && i < maxi && j < maxj))

    vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int color)
    {
        int                  orig = image[sr][sc];
        int                  maxi = image.size(), maxj = image[0].size();
        vector<vector<bool>> visited(maxi, vector<bool>(maxj, false));

        queue<pair<int, int>> q;
        q.push({sr, sc});
        visited[sr][sc] = true;

        // mark start position as new color
        image[sr][sc] = color;
        while (!q.empty())
        {
            int qsize = q.size();
            while (qsize--)
            {
                auto [i, j] = q.front();
                q.pop();
                // iterate neighbors
                for (auto [newi, newj] :
                     vector<pair<int, int>>{{i + 1, j}, {i - 1, j}, {i, j + 1}, {i, j - 1}})
                {
                    if (VALID(newi, newj, maxi, maxj) && image[newi][newj] == orig &&
                        !visited[newi][newj])
                    {
                        visited[newi][newj] = true;
                        image[newi][newj]   = color;  // marked as used
                        q.push({newi, newj});
                    }
                }
            }
        }

        return image;
    }
};
// @lc code=end
