# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = -math.inf
        
        def inOrder(root):
            if not root:
                return True
            if not inOrder(root.left):
                return False
            nonlocal prev
            if root.val <= prev:
                return False
            prev = root.val
            return inOrder(root.right)
        
        return inOrder(root)