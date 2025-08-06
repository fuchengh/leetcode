/*
 * @lc app=leetcode id=189 lang=cpp
 *
 * [189] Rotate Array
 */

#include "lib/headers.h"

// @lc code=start
class Solution
{
  public:
    void rotate(vector<int> &nums, int k)
    {
        // try solving with stl reverse
        // original: using my reverse
        int n = nums.size();
        k %= n;
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin()+k);
        reverse(nums.begin()+k, nums.end());
    }
};
// @lc code=end
