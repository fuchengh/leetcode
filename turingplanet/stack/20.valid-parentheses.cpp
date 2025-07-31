/*
 * @lc app=leetcode id=20 lang=cpp
 *
 * [20] Valid Parentheses
 */

#include "lib/headers.h"

// @lc code=start
class Solution
{
  public:
    bool validClose(char c, stack<char> &cur)
    {
        if (cur.empty())
            return false;
        if (c == ')' && cur.top() != '(')
            return false;
        if (c == ']' && cur.top() != '[')
            return false;
        if (c == '}' && cur.top() != '{')
            return false;
        return true;
    }
    bool isValid(string s)
    {
        // for close parentheses ) ] }, we check if the top of stack is its open par.
        stack<char> cur;
        for (char c : s)
        {
            switch (c)
            {
                case ')':
                    [[fallthrough]];  // intentional fallthrough
                case '}':
                    [[fallthrough]];  // intentional fallthrough
                case ']':
                    if (!validClose(c, cur))
                        return false;
                    // valid, pop cur stack
                    cur.pop();
                    break;
                default:
                    // is open pars, insert
                    cur.push(c);
                    break;
            }
        }
        // we need to pair all pars to make it valid
        return cur.empty();
    }
};
// @lc code=end
