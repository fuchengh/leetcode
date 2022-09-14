# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        q = deque([root])
        levels = []
        if not root:
            return []
        
        while q:
            q_len = len(q)
            levels.append([])
            
            for i in range(q_len):
                cur = q.popleft()
                levels[level].append(cur.val)
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            level += 1
        
        return levels
        