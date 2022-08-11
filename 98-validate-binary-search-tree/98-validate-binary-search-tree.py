# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # run inorder traversal
        nodes = []
        
        def inOrder(node):
            if node.left:
                inOrder(node.left)
            nodes.append(node.val)
            if node.right:
                inOrder(node.right)
        
        inOrder(root)
        
        return nodes == sorted(nodes) and len(nodes) == len(set(nodes))