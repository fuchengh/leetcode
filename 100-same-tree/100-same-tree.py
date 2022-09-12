# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inOrder(root, seen):
            if not root:
                return
            if root.left:
                seen.append(root.left.val)
                inOrder(root.left, seen)
            else:
                seen.append(None)
            seen.append(root.val)
            if root.right:
                seen.append(root.right.val)
                inOrder(root.right, seen)
            else:
                seen.append(None)
        
        seen_p = []
        seen_q = []
        inOrder(p, seen_p)
        inOrder(q, seen_q)
        
        return seen_p == seen_q