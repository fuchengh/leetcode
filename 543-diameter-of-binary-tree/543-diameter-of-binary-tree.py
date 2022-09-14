# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def longest(node):
            if not node:
                return 0
            left = longest(node.left)
            right = longest(node.right)
            
            self.ans = max(self.ans, left + right)
            
            return max(left, right) + 1
        
        longest(root)
        return self.ans