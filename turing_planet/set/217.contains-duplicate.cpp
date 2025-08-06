/*
 * @lc app=leetcode id=217 lang=cpp
 *
 * [217] Contains Duplicate
 */

// @lc code=start
class Solution
{
  public:
    bool containsDuplicate(vector<int> &nums)
    {
        unordered_set<int> seen;
        for (int i : nums)
        {
            if (seen.count(i))
                return true;
            seen.insert(i);
        }
        return false;
    }
};
// @lc code=end
