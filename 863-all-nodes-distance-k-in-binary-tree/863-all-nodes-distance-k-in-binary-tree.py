# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        conn_table = defaultdict(list)
        def connect(p, c):
            if p and c:
                conn_table[p.val].append(c.val)
                conn_table[c.val].append(p.val)
            if c.left: connect(c, c.left)
            if c.right: connect(c, c.right)
        
        connect(None, root)
        bfs = [target.val]
        seen = set(bfs)
        for i in range(k):
            new_level = []
            for node in bfs:
                for connected_node in conn_table[node]:
                    if connected_node not in seen:
                        new_level.append(connected_node)
            bfs = new_level
            for val in bfs:
                seen.add(val)
        return bfs