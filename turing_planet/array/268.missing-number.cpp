/*
 * @lc app=leetcode id=268 lang=cpp
 *
 * [268] Missing Number
 */

// @lc code=start
class Solution
{
  public:
    int missingNumber(vector<int> &nums)
    {
        int n       = nums.size();
        int sum     = (n * (n + 1)) / 2;
        int cur_sum = accumulate(nums.begin(), nums.end(), 0);

        return sum - cur_sum;
    }
};
// @lc code=end
