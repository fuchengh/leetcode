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
        
        def clone(node):
            if not node:
                return
            if node.val in seen:
                return seen[node.val]
            clone_node = Node(node.val, [])
            seen[node.val] = clone_node
            
            if node.neighbors:
                clone_node.neighbors = [clone(n) for n in node.neighbors]
            
            return clone_node
        
        return clone(node)