class MinStack:
    def __init__(self):
        self.s = []
        self.mins = []
        
    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            curr_min = self.mins[-1]
            if curr_min >= val:
                self.mins.append(val)
        
    def pop(self) -> None:
        if self.mins[-1] == self.s[-1]:
            del self.mins[-1]
        del self.s[-1]
        
    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()