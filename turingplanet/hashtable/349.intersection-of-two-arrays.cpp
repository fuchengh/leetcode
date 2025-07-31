/*
 * @lc app=leetcode id=349 lang=cpp
 *
 * [349] Intersection of Two Arrays
 */

#include "lib/headers.h"

// @lc code=start
class Solution
{
  public:
    vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
    {
        unordered_set<int> set1(nums1.begin(), nums1.end());
        unordered_set<int> set2(nums2.begin(), nums2.end());
        vector<int>        res;
        if (set1.size() < set2.size())
        {
            for (int i : set2)
                if (set1.count(i))
                    res.push_back(i);
        }
        else
        {
            for (int i : set1)
                if (set2.count(i))
                    res.push_back(i);
        }

        return res;
    }
};
// @lc code=end
