# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        
        while q:
            cur = q.popleft()
            if cur:
                left = right = None
                if cur.left:
                    q.append(cur.left)
                    left = cur.left
                if cur.right:
                    q.append(cur.right)
                    right = cur.right
                cur.left = right
                cur.right = left
    
        return root
            