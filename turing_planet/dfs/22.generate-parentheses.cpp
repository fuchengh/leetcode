/*
 * @lc app=leetcode id=22 lang=cpp
 *
 * [22] Generate Parentheses
 */

#include "lib/headers.h"

// @lc code=start
class Solution
{
  private:
    void dfs(vector<string> &res, string &cur, int n, int open, int close)
    {
        if (cur.size() == 2 * n)
        {
            // terminate condition
            res.push_back(cur);
            return;
        }
        if (open < n)
        {
            // we can still insert open
            string tmp = cur + '(';
            dfs(res, tmp, n, open + 1, close);
        }
        if (close < open)
        {
            // we can still insert close
            string tmp = cur + ')';
            dfs(res, tmp, n, open, close + 1);
        }
    }

  public:
    vector<string> generateParenthesis(int n)
    {
        vector<string> res;
        string         cur = "";
        dfs(res, cur, n, 0, 0);

        return res;
    }
};
// @lc code=end
