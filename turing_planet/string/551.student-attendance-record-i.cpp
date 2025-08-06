/*
 * @lc app=leetcode id=551 lang=cpp
 *
 * [551] Student Attendance Record I
 */

#include "lib/headers.h"

// @lc code=start
class Solution {
public:
    bool checkRecord(string s) {
        int absent = 0;
        int late   = 0;
        for (char c : s)
        {
            if (c == 'P' || c == 'A')
            {
                // check late and reset
                if (late >= 3)
                    return false;
                late = 0;
                // update absent if c is A
                if (c == 'A')
                    absent++;
            }
            else  // is late
            {
                late++;
                if (late >= 3)
                    return false;
            }
        }
        return absent < 2;
    }
};
// @lc code=end

