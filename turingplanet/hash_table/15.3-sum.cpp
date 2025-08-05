/*
 * @lc app=leetcode id=15 lang=cpp
 *
 * [15] 3Sum
 */
#include "lib/headers.h"

// @lc code=start
class Solution
{
  public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        int n = nums.size();

        for (int i = 0; i < n - 2; i++)
        {
            if (nums[i] > 0)
                break;  // not possible to find value
            if (i > 0 && nums[i] == nums[i - 1])
                continue;  // already processed

            int j = i + 1, k = n - 1;
            while (j < k)
            {
                long sum = static_cast<long>(nums[i]) + nums[j] + nums[k];
                if (sum == 0)
                {
                    res.push_back({nums[i], nums[j], nums[k]});
                    // shrink the search window
                    while (j < k && nums[j] == nums[j + 1])
                        j++;
                    while (j < k && nums[k] == nums[k - 1])
                        k--;
                    // move to next number
                    j++;
                    k--;
                }
                else if (sum < 0)
                {
                    // need a larger j
                    j++;
                }
                else
                {
                    // need a smaller k
                    k--;
                }
            }
        }
        return res;
    }
};
// @lc code=end
