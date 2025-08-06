/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

#include "lib/headers.h"

// @lc code=start
class Solution
{
  public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++)
        {
            int remain = target - nums[i];
            if (seen.count(remain))
                return {seen[remain], i};
            seen[nums[i]] = i;
        }
        return {};
    }
};
// @lc code=end
