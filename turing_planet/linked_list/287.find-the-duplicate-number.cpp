/*
 * @lc app=leetcode id=287 lang=cpp
 *
 * [287] Find the Duplicate Number
 */

// @lc code=start
class Solution
{
  public:
    int findDuplicate(vector<int> &nums)
    {
        int slow = nums[0], fast = nums[0];
        do
        {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);  // find where the cycle happens

        int p1 = nums[0];
        int p2 = slow;
        while (p1 != p2)
        {
            p1 = nums[p1];
            p2 = nums[p2];
        }

        return p1;
    }
};
// @lc code=end
