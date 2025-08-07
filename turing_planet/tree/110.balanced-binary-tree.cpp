/*
 * @lc app=leetcode id=110 lang=cpp
 *
 * [110] Balanced Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution
{
  public:
    int height(TreeNode *root)
    {
        // return -1 if height is not balanced
        if (!root)
            return 0;
        int left = height(root->left);
        if (left < 0)
            return -1;
        int right = height(root->right);
        if (right < 0)
            return -1;
        if (abs(right - left) > 1)  // not balanced!!
            return -1;
        return max(left, right) + 1;  // is balanced, return the current path's depth
    }

    bool isBalanced(TreeNode *root) { return height(root) >= 0; }
};
// @lc code=end
