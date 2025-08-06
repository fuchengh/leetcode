/*
 * @lc app=leetcode id=941 lang=cpp
 *
 * [941] Valid Mountain Array
 */

#include "lib/headers.h"

// @lc code=start
class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        bool increasing = false, decreasing = false;
        for (int i = 1; i < arr.size(); i++)
        {
            if (arr[i] == arr[i - 1])
            {
                // flat
                return false;
            }
            else if (arr[i] > arr[i - 1])
            {
                increasing = true;
                if (decreasing)
                    return false;
            }
            else
            {
                decreasing = true;
            }
        }

        return increasing && decreasing;
    }
};
// @lc code=end

