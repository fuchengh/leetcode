class Solution:
    def breakPalindrome(self, p: str) -> str:
        if len(p) <= 1:
            return ""
        
        char = defaultdict(lambda: 0)
        for c in p:
            char[c] += 1
        
        list_p = list(p)
        
        # if p has format of a+ x a+, change last a to b
        if char["a"] == len(p)-1 or char["a"] == len(p):
            list_p[-1] = "b"
        # other formats, change first non a to a
        else:
            for i, c in enumerate(list_p):
                if c != "a":
                    list_p[i] = "a"
                    break
        return "".join(list_p)