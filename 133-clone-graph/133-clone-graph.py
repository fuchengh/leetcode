"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = {}
        q = deque([node])
        
        if not node:
            return
        
        while q:
            cur = q.popleft()
            if cur not in seen:
                seen[cur] = Node(cur.val, [])
            for n in cur.neighbors:
                if n not in seen:
                    seen[n] = Node(n.val, [])
                    q.append(n)
                seen[cur].neighbors.append(seen[n])
        return seen[node]