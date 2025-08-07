/*
 * @lc app=leetcode id=125 lang=cpp
 *
 * [125] Valid Palindrome
 */

// @lc code=start
class Solution
{
  public:
    bool isPalindrome(string s)
    {
        int l = 0;
        int r = s.size() - 1;
        while (l < r)
        {
            // find first alphanum for l
            while (!isalnum(s[l]) && l < r)
                l++;
            while (!isalnum(s[r]) && l < r)
                r--;
            if (tolower(s[l]) != tolower(s[r]))
                return false;
            l++;
            r--;
        }
        return true;
    }
};
// @lc code=end
