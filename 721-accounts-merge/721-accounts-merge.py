class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        table = {}
        
        for acc in accounts:
            name = acc[0]
            to_merge = set(acc[1:])
            if name not in table:
                table[name] = [to_merge]
            else:
                idx = 0
                while idx < len(table[name]):
                    sets = table[name][idx]
                    if not sets.isdisjoint(to_merge): # need to merge, del this set
                        to_merge |= sets
                        del table[name][idx]
                        idx -= 1
                    idx += 1
                table[name].append(to_merge)
        
        res = []
        for name, sets in table.items():
            for s in sets:
                cur = [name]
                cur.extend(sorted(list(s)))
                res.append(cur)
        
        return res