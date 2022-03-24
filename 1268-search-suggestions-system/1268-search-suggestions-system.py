class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def find(arr, prefix):
            i = 0
            j = len(arr)
            while i < j:
                mid = (i+j) // 2
                if arr[mid] >= prefix:
                    j = mid
                else:
                    i = mid + 1
            return i
        products.sort()
        res = []
        prefix = ""
        curr_idx = 0
        for c in searchWord:
            prefix += c
            # find word that starts with prefix using bsearch
            first_idx = find(products[curr_idx:], prefix) + curr_idx
            this_row = []
            for i in range(first_idx, first_idx+3):
                if i >= len(products): break
                if products[i].startswith(prefix):
                    this_row.append(products[i])
                    
            res.append(this_row)
            curr_idx = first_idx
        
        return res
           
