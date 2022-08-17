class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        
        for s in strs:
            key = str(sorted(list(s)))
            table[key].append(s)
        
        return table.values()
                