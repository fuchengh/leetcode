# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def preOrder(root, path):
            if not root:
                return
            path.append(root.val)
            preOrder(root.left, path)
            preOrder(root.right, path)
            if not root.left and not root.right:
                if sum(path) == targetSum:
                    nonlocal res
                    res.append(path[::])
            path.pop()
        
        if not root:
            return []
        
        preOrder(root, [])
        return res