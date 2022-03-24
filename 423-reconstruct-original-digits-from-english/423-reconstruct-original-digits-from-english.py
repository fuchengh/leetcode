class Solution:
    def originalDigits(self, s: str) -> str:
        table = defaultdict(lambda: 0)
        out = {}
        
        for c in s:
            table[c] += 1
        
        out["0"] = table["z"]
        out["2"] = table["w"]
        out["4"] = table["u"]
        out["6"] = table["x"]
        out["8"] = table["g"]
        
        out["3"] = table["h"] - out["8"]
        out["5"] = table["f"] - out["4"]
        out["7"] = table["s"] - out["6"]
        
        out["9"] = table["i"] - out["5"] - out["6"] - out["8"]
        out["1"] = table["n"] - out["7"] - 2*out["9"]
        
        res = ""
        for i in "0123456789":
            if out[i] > 0:
                res += i * out[i]
        
        return res