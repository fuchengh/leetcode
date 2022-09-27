# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def longest(node):
            if not node:
                return 0
            
            l = longest(node.left)
            r = longest(node.right)
            nonlocal ans
            ans = max(ans, l + r)
            return max(l, r) + 1
        
        longest(root)
        return ans