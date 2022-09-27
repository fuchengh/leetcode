class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        left = set()
        right = set()
        
        ptr = len(dominoes)-1
        symbols = [None for _ in range(len(dominoes))]
        
        while ptr >= 0:
            if dominoes[ptr] == "L":
                # push until it reaches an "R"
                while ptr >= 0 and dominoes[ptr] != "R":
                    symbols[ptr] = "L"
                    ptr -= 1
            ptr -= 1
        
        marked = []
        ptr = 0
        
        while ptr < len(dominoes):
            if dominoes[ptr] == "R":
                while ptr < len(dominoes) and dominoes[ptr] != "L":
                    if symbols[ptr] == "L":
                        symbols[ptr] += "R"
                        if ptr >= 1 and symbols[ptr-1] == "LR":
                            marked[-1][1] = ptr
                        elif ptr >= 1 and symbols[ptr-1] != "LR":
                            marked.append([ptr, ptr])
                    else:
                        symbols[ptr] = "R"
                    ptr += 1
            ptr += 1
        
        for mark in marked:
            range_ = mark[1] - mark[0] + 1
            if mark[0] == mark[1]:
                symbols[mark[0]] = "."
            elif (range_) % 2 == 0:
                # set left half to be "R"
                for left in range(mark[0], mark[0] + range_//2):
                    symbols[left] = "R"
                for right in range(mark[0]+range_//2, mark[1]+1):
                    symbols[right] = "L"
            elif (range_) % 2 != 0:
                mid = (mark[0] + mark[1]) // 2
                for left in range(mark[0], mid):
                    symbols[left] = "R"
                for right in range(mid+1, mark[1]+1):
                    symbols[right] = "L"
                symbols[mid] = "."
        
        return "".join([x if x else "." for x in symbols])