# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check if two trees are the same
        def isSame(p, q):
            if not p and not q:
                return True
            if p and q:
                return (p.val == q.val) and \
                    isSame(p.left, q.left) and \
                    isSame(p.right, q.right)
            
            return False
        
        # find starting node
        q = deque([root])
        
        while q:
            cur = q.popleft()
            if cur.val == subRoot.val:
                if isSame(cur, subRoot):
                    return True
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        
        return False