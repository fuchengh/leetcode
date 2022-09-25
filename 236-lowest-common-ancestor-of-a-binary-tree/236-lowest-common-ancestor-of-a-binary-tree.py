# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            mid = (node.val == p.val or node.val == q.val)
            
            if (mid and left) or (mid and right) or (left and right) or (mid and left and right):
                self.ans = node
            
            return mid or left or right
    
        dfs(root)
        return self.ans