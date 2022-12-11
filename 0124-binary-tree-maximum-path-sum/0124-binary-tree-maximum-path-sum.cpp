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
class Solution {
public:
    unordered_map<TreeNode*, int> cache;
    int cal_max_path(TreeNode *node) {
        if(!node) return 0;
        if(cache.count(node)) return cache[node];
        int left = cal_max_path(node->left);
        int right = cal_max_path(node->right);
        int ans = max(max(left, right) + node->val, node->val); // take max of l, r or not take
        cache[node] = ans;
        return ans;
    }

    int maxPathSum(TreeNode* root) {
        cal_max_path(root);
        int ans = INT_MIN;
        for(auto [k, v]: cache) {
            int left = k->left ? cache[k->left] : 0;
            int right = k->right ? cache[k->right] : 0;
            int left_root_right = k->val + left + right;
            int left_root = k->val + left;
            int root_right = k->val + right;
            int root_only = k->val;
            // find largest condition (root, root+left+right, root+left, root+right)
            int cur = max(max(left_root_right, left_root), max(root_right, root_only));
            ans = max(ans, cur);
        }
        return ans;
    }
};