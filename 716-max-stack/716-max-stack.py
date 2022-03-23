class MaxStack:

    def __init__(self):
        self.stack = []
        self.maxstack = []
        

    def push(self, x: int) -> None:
        if len(self.maxstack) > 0:
            if x > self.maxstack[-1]:
                self.maxstack.append(x)
            else:
                self.maxstack.append(self.maxstack[-1])
        else:
            self.maxstack.append(x)
        
        self.stack.append(x)

    def pop(self) -> int:
        # return and delete last element
        self.maxstack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxstack[-1]

    def popMax(self) -> int:
        # pop stack until getting the max val
        m = self.maxstack[-1]
        temp = []
        while self.stack[-1] != m:
            temp.append(self.pop())
        
        self.pop() # delete max item
        temp = temp[::-1]
        # push back temp stack to original stack
        for t in temp:
            self.push(t)
        
        return m


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()