# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
            
        def search(root):
            if not root:
                return
            if p.val > root.val and q.val > root.val:
                return search(root.right)
            elif p.val < root.val and q.val < root.val:
                return search(root.left)
            elif p.val <= root.val <= q.val:
                return root
            
            search(root.left)
            search(root.right)
            
        return search(root)