# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def builder(left, right):
            nonlocal idx
            if idx == n: return None
            
            val = preorder[idx]
            if val < left or val > right: return None
            idx += 1
            root = TreeNode(val)
            root.left = builder(left, val)
            root.right = builder(val, right)
            return root
        
        idx = 0
        n = len(preorder)
        return builder(-math.inf, math.inf)