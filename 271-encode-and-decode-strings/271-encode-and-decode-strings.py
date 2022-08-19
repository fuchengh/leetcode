class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enc = ""
        for s in strs:
            str_len = "%04d" % len(s)
            enc += str_len + s
        return enc

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        ptr = 0
        
        while ptr < len(s):
            str_len = int(s[ptr:ptr+4])
            string = s[ptr+4: ptr+4+str_len]
            res.append(string)
            ptr += str_len + 4
            
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))