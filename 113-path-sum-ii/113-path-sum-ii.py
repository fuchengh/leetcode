# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, res, target, root, path):
        if not root:
            return
        path.append(root.val)
        self.preOrder(res, target, root.left, path)
        self.preOrder(res, target, root.right, path)
        if not root.left and not root.right:
            if sum(path) == target:
                res.append(path[::])
        path.pop()
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        self.preOrder(res, targetSum, root, [])
        return res