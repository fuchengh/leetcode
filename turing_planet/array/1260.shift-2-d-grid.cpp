/*
 * @lc app=leetcode id=1260 lang=cpp
 *
 * [1260] Shift 2D Grid
 */

#include "lib/headers.h"

// @lc code=start
class Solution
{
  public:
    vector<vector<int>> shiftGrid(vector<vector<int>> &grid, int k)
    {
        int m = grid.size(), n = grid[0].size();
        vector<int> flatten;
        for (auto &v : grid)
        {
            for (int val : v)
            {
                flatten.push_back(val);
            }
        }
        // rotate flatten to right by k
        k %= (m*n);
        // try using stl rotate, default is rotate to left, so we should do it in-reverse
        rotate(flatten.rbegin(), flatten.rbegin()+k, flatten.rend());

        vector<vector<int>> res(m, vector<int>(n, 0));
        // push result back
        int p = 0;
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                res[i][j] = flatten[p++];
            }
        }

        return res;
    }
};
// @lc code=end
