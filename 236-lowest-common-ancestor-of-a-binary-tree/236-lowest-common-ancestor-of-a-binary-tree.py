# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, target, path):
            if not node:
                return
            path.append(node)
            dfs(node.left, target, path)
            dfs(node.right, target, path)
            if node.val == target:
                if target == p.val:
                    path_p[:] = path
                else:
                    path_q[:] = path
                return
            path.pop()
        
        path_p = []
        path_q = []
        dfs(root, p.val, [])
        dfs(root, q.val, [])

        ancestor_p = defaultdict(lambda: None)
        for node_p in path_p[::-1]:
            ancestor_p[node_p.val] = node_p
        
        for node_q in path_q[::-1]:
            if ancestor_p[node_q.val]:
                return node_q