class MinStack:
    def __init__(self):
        self.s = [] # s[i][0]: value, s[i][1]: cur min

    def push(self, val: int) -> None:
        cur_min = math.inf
        if self.s:
            cur_min = self.s[-1][1]
        self.s.append((val, min(val, cur_min)))

    def pop(self) -> None:
        self.s.pop()
        

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()