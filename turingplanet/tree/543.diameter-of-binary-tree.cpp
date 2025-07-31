/*
 * @lc app=leetcode id=543 lang=cpp
 *
 * [543] Diameter of Binary Tree
 */

#include "lib/headers.h"

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
    int ans = 0;
    int dfs(TreeNode *root)
    {
        if (!root)
            return 0;
        int left  = dfs(root->left);
        int right = dfs(root->right);
        cout << "Working on " << root->val << ":\n";
        cout << "Path of left has " << left << ',';
        cout << "Path of right has " << right << '\n';
        int len = left + right;
        ans     = max(ans, len);
        return 1 + max(left, right);
    }

    int diameterOfBinaryTree(TreeNode *root)
    {
        if (!root)
            return 0;
        dfs(root);
        return ans;
    }
};
// @lc code=end
