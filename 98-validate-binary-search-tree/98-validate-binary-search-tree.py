# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        path = []
        
        def inOrder(node):
            if not node:
                return
            nonlocal path
            if node.left:
                inOrder(node.left)
            path.append(node.val)
            if node.right:
                inOrder(node.right)
            
        inOrder(root)
        for i in range(1, len(path)):
            if path[i-1] >= path[i]:
                return False
        return True