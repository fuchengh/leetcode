# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level_table = defaultdict(lambda: 0)
        parent_table = defaultdict(lambda: TreeNode)
        
        s = [root]
        
        while s:
            cur = s.pop()
            level_table[cur] = level_table[parent_table[cur]] + 1
            if cur.left:
                parent_table[cur.left] = cur
                s.append(cur.left)
            if cur.right:
                parent_table[cur.right] = cur
                s.append(cur.right)
        
        res = [v for k, v in level_table.items()]
        
        return max(res)