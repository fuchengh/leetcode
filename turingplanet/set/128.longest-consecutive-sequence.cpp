/*
 * @lc app=leetcode id=128 lang=cpp
 *
 * [128] Longest Consecutive Sequence
 */

#include "lib/headers.h"

// @lc code=start
class Solution
{
  public:
    int longestConsecutive(vector<int> &nums)
    {
        unordered_set<int> vals(nums.begin(), nums.end());
        int                ans = 0;

        for (int i : vals)
        {
            int len = 1, cur = i;
            if (!vals.count(cur - 1))  //prevent duplicate check
            {
                while (vals.count(cur + 1))
                {
                    cur = cur + 1;
                    len++;
                }
            }
            ans = max(len, ans);
        }
        return ans;
    }
};
// @lc code=end
