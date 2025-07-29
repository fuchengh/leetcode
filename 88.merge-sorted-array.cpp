/*
 * @lc app=leetcode id=88 lang=cpp
 *
 * [88] Merge Sorted Array
 */

#include "lib/headers.h"

// @lc code=start
class Solution
{
  public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        int p = (m + n - 1);
        int i = m - 1;
        int j = n - 1;
        while (p >= 0)
        {
            int cand_1 = i >= 0 ? nums1[i] : INT_MIN;
            int cand_2 = j >= 0 ? nums2[j] : INT_MIN;
            if (cand_1 >= cand_2)
            {
                nums1[p] = cand_1;
                i--;
            }
            else
            {
                nums1[p] = cand_2;
                j--;
            }
            p--;
        }
    }
};
// @lc code=end
