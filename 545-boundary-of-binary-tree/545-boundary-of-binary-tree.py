# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left_boundary = []
        right_boundary = []
        leaves = []
        
        def preorder(node, flag):
            if not node:
                return
            if isRightBoundary(flag):
                right_boundary.append(node.val)
            elif isLeftBoundary(flag) or isRoot(flag):
                left_boundary.append(node.val)
            elif isLeaf(node):
                leaves.append(node.val)
            
            if node.left:
                preorder(node.left, leftFlag(node, flag))
            if node.right:
                preorder(node.right, rightFlag(node, flag))
        
        def isLeaf(node):
            return not node.right and not node.left
        def isRightBoundary(flag):
            return flag == 2
        def isLeftBoundary(flag):
            return flag == 1
        def isRoot(flag):
            return flag == 0
        def leftFlag(node, flag):
            if isLeftBoundary(flag) or isRoot(flag):
                return 1
            if isRightBoundary(flag) and not node.right:
                return 2
            return 3
        def rightFlag(node, flag):
            if isRightBoundary(flag) or isRoot(flag):
                return 2
            if isLeftBoundary(flag) and not node.left:
                return 1
            return 3
        
        
        
        preorder(root, 0)
        left_boundary.extend(leaves)
        left_boundary.extend(right_boundary[::-1])
        return left_boundary