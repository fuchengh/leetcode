/*
 * @lc app=leetcode id=15 lang=cpp
 *
 * [15] 3Sum
 */

// @lc code=start
class Solution
{
  public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());

        int n = nums.size();
        for (int i = 0; i < n; i++)
        {
            // not possible to make it zero
            if (nums[i] > 0)
                break;
            // skip duplicate i's
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            int j = i + 1;
            int k = n - 1;
            while (j < k)
            {
                long sum = static_cast<long>(nums[i]) + nums[j] + nums[k];
                if (sum == 0)
                {
                    res.push_back({nums[i], nums[j], nums[k]});
                    // we already checked nums[j] and nums[k], find a new value
                    while (j < k && nums[j] == nums[j + 1])
                        j++;
                    while (j < k && nums[k] == nums[k - 1])
                        k--;
                    // move to next j and k
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
                    k--;
                }
            }
        }
        return res;
    }
};
// @lc code=end
