# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def sortlist(arr):
            sort_by_row = defaultdict(list)
            for elem in arr:
                val, row = elem
                sort_by_row[row].append(val)
            # output result and sort dict[row] as well
            res = []
            for key in sorted(sort_by_row.keys()):
                curr_row = sort_by_row[key]
                curr_row.sort() # sort same position by value
                res.extend(curr_row)
            return res
            
        cols = defaultdict(list)
        q = deque([(root, 0, 0)])
        
        while q:
            node, row, col = q.popleft()
            cols[col].append((node.val, row))
            if node.left:
                q.append((node.left, row+1, col-1))
            if node.right:
                q.append((node.right, row+1, col+1))
        
        # output result
        res = []
        for col_idx in sorted(cols.keys()):
            curr_col = sortlist(cols[col_idx])
            res.append([x for x in curr_col])
        return res
        
            